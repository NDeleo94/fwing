from django.contrib import admin

from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from django.contrib.auth.models import Group
from apps.fw.models.user_model import FwUser
from apps.fw.models.egreso_model import Egreso
from apps.fw.models.actividad_model import Actividad
from apps.fw.models.carrera_model import Carrera

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = FwUser
        fields = ("dni",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            "<a href=../password>this form</a>."
        ),
    )

    class Meta:
        model = FwUser
        fields = ("dni", "password", "is_active", "is_admin")


class EgresadoCarreraInline(admin.TabularInline):
    model = Egreso
    extra = 1


class ActividadInline(admin.TabularInline):
    model = Actividad
    extra = 1
    fields = (
        "organizacion",
        "puesto",
        "inicio",
        "fin",
    )


class FwUserResources(resources.ModelResource):
    class Meta:
        model = FwUser
        fields = (
            "id",
            "dni",
            "apellidos",
            "nombres",
            "email",
            "fecha_nac",
            "nacionalidad",
            "ciudad_natal",
            "ciudad_actual",
            "domicilio",
            "sexo",
        )

    def import_row(
        self, row, instance_loader, using_transactions=True, dry_run=False, **kwargs
    ):
        # Create FwUser object
        fwUser = super().import_row(
            row, instance_loader, using_transactions, dry_run, **kwargs
        )
        usuario = FwUser.objects.get(id=fwUser.object_id)
        # Check if the required fields for Egreso are present in the row
        if "carrera" in row and "ciclo_egreso" in row:
            # Retrieve or create Carrera object based on carrera
            carrera_id = row["carrera"]
            carrera = Carrera.objects.get(id=carrera_id)
            # Create Egreso object and set the foreign keys
            Egreso.objects.create(
                usuario=usuario,
                carrera=carrera,
                ciclo_egreso=row["ciclo_egreso"],
            )

        return fwUser


class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    inlines = [
        EgresadoCarreraInline,
        ActividadInline,
    ]
    list_display = (
        "dni",
        "apellidos",
        "nombres",
        "email",
        "is_active",
    )
    list_filter = (
        "is_active",
        "sexo",
    )
    fieldsets = (
        # (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "dni",
                    "apellidos",
                    "nombres",
                    "email",
                    "nacionalidad",
                    "fecha_nac",
                    "ciudad_natal",
                    "ciudad_actual",
                    "domicilio",
                    "certificado",
                    "imagen",
                    "sexo",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_admin", "is_superuser", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "dni",
                    "apellidos",
                    "nombres",
                    "password1",
                    "password2",
                    "email",
                    "nacionalidad",
                    "fecha_nac",
                    "ciudad_natal",
                    "ciudad_actual",
                    "domicilio",
                    "certificado",
                    "imagen",
                    "sexo",
                ),
            },
        ),
    )
    search_fields = (
        "dni",
        "apellidos",
        "nombres",
        "email",
    )
    ordering = ("email",)
    filter_horizontal = ("user_permissions",)
    resource_class = FwUserResources


# Now register the new UserAdmin...
admin.site.register(FwUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
