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
from apps.fw.models.ciudad_model import Ciudad
from apps.fw.models.privacidad_model import Privacidad

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget


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
    id = Field(attribute="id", column_name="ID")
    dni = Field(attribute="dni", column_name="DNI")
    nombres = Field(attribute="nombres", column_name="NOMBRES")
    apellidos = Field(attribute="apellidos", column_name="APELLIDOS")
    email = Field(attribute="email", column_name="EMAIL")
    fecha_nac = Field(attribute="fecha_nac", column_name="FECHA_NAC")
    nacionalidad = Field(attribute="nacionalidad", column_name="NACIONALIDAD")
    sexo = Field(attribute="sexo", column_name="SEXO")
    # ciudad_natal = Field(attribute="ciudad_natal", column_name="LOCALIDAD")
    # ciudad_actual = Field(attribute="ciudad_actual", column_name="LOCALIDAD")
    # domicilio = Field(attribute="domicilio", column_name="DOMICILIO")
    carrera = Field(attribute="carrera", column_name="CARRERA")
    ciclo_egreso = Field(attribute="ciclo_egreso", column_name="EGRESO")

    ciudad_natal = Field(
        column_name="LOCALIDAD",
        attribute="ciudad_natal",
        widget=ForeignKeyWidget(Ciudad, field="ciudad"),
    )
    ciudad_actual = Field(
        column_name="LOCALIDAD",
        attribute="ciudad_actual",
        widget=ForeignKeyWidget(Ciudad, field="ciudad"),
    )

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

    def before_import_row(self, row, **kwargs):
        print(1)
        try:
            # for key, value in row.items():
            #     if isinstance(value, str):
            #         row[key] = value.title()
            row["NOMBRES"] = row["NOMBRES"].title()
            row["APELLIDOS"] = row["APELLIDOS"].title()
            row["NACIONALIDAD"] = row["NACIONALIDAD"].title()
        except Exception as e:
            print(e)

        try:
            ciudad = Ciudad.objects.filter(ciudad__icontains=row["LOCALIDAD"]).first()
            if ciudad:
                row["LOCALIDAD"] = ciudad
            else:
                row["LOCALIDAD"] = None
        except Exception as e:
            print(e)

        return row

    def skip_row(self, instance, original, row, import_validation_errors=None):
        print(2)
        return (
            True
            if FwUser.objects.filter(
                dni=instance.dni,
            ).exists()
            else False
        )

    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        print(3)
        dni = row["DNI"]
        carrera_id = row["CARRERA"]

        egreso = row["EGRESO"]

        try:
            usuario = FwUser.objects.filter(dni=dni).first()
            carrera = Carrera.objects.filter(id=carrera_id).first()

            Privacidad.objects.create(usuario=usuario)

            Egreso.objects.create(
                usuario=usuario,
                carrera=carrera,
                ciclo_egreso=egreso,
            )
        except Exception as e:
            print(e)


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
        "id",
        "apellidos",
        "nombres",
        "dni",
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
                    "sexo",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login",),
            },
        ),
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
    ordering = (
        "apellidos",
        "nombres",
        "dni",
        "email",
    )
    filter_horizontal = ("user_permissions",)
    resource_class = FwUserResources


# Now register the new UserAdmin...
admin.site.register(FwUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
