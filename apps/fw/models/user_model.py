from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class FwUserManager(BaseUserManager):
    def create_user(self, dni, password=None):
        """
        Creates and saves a User with the given dni and password.
        """
        if not dni:
            raise ValueError("Users must have an dni")

        user = self.model(
            dni=dni,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, password=None):
        """
        Creates and saves a superuser with the given dni and password.
        """
        user = self.create_user(
            dni,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class FwUser(AbstractBaseUser, PermissionsMixin):
    dni = models.BigIntegerField(
        verbose_name="Numero de documento",
        unique=True,
        validators=[
            MinValueValidator(1000000),
        ],
    )
    email = models.EmailField(
        verbose_name="Correo Electronico",
        max_length=255,
        blank=True,
        null=True,
    )
    nombres = models.CharField(
        "Nombres",
        max_length=200,
        blank=False,
        null=False,
    )
    apellidos = models.CharField(
        "Apellidos",
        max_length=200,
        blank=False,
        null=False,
    )
    fecha_nac = models.DateField(
        "Fecha de Nacimiento",
        blank=True,
        null=True,
    )
    nacionalidad = models.CharField(
        "Nacionalidad",
        max_length=200,
        blank=True,
        null=True,
    )
    ciudad_natal = models.ForeignKey(
        "Ciudad",
        related_name="ciudad_natal",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    ciudad_actual = models.ForeignKey(
        "Ciudad",
        related_name="ciudad_actual",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    domicilio = models.CharField(
        "Domicilio",
        max_length=200,
        blank=True,
        null=True,
    )
    certificado = models.CharField(
        "Certificado",
        max_length=200,
        blank=True,
        null=True,
    )
    sexo = models.CharField(
        "Sexo",
        max_length=1,
        choices=(
            ("F", "Femenino"),
            ("M", "Masculino"),
        ),
        blank=True,
        null=True,
    )
    origen = models.IntegerField(
        "Subido desde",
        choices=(
            (1, "ARCHIVO"),
            (2, "SIU"),
            (3, "FW"),
        ),
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_admin = models.BooleanField(
        "staff status",
        default=False,
        help_text=("Designates whether the user can log into this admin site."),
    )

    objects = FwUserManager()

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = [
        "apellidos",
        "nombres",
    ]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self) -> str:
        return f"{self.apellidos}, {self.nombres}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
