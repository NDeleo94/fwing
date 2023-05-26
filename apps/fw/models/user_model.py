from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class FwUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
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
        unique=True,
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
    ciudad_natal = models.CharField(
        "Ciudad natal",
        max_length=200,
        blank=True,
        null=True,
    )
    ciudad_actual = models.CharField(
        "Ciudad actual",
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
    REQUIRED_FIELDS = []

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
