from django.db import models
from main.models import Base
from django.utils.text import slugify

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group


# Create You models here

class AccessLevel:
    """
        Access level for Users roles
    """

    SUPER_ADMIN = 800
    IS_COMPANY = 600  # SIMPLE WORD COMPANY is basically use for yarn Companies
    IS_CARGO_COMPANY = 400
    CUSTOMER = 300

    SUPER_ADMIN_CODE = "super_admin"
    IS_COMPANY_CODE = 'is_company'
    IS_CARGO_COMPANY_CODE = 'is_cargo_company'
    CUSTOMER_CODE = "is_customer"

    CHOICES = (
        (SUPER_ADMIN, "Super_admin"),
        (IS_COMPANY, "Company"),
        (IS_CARGO_COMPANY, "Cargo_company")
    )
    CODES = (
        (SUPER_ADMIN, "super_admin"),
        (IS_COMPANY, 'is_company'),
        (IS_CARGO_COMPANY, 'is_cargo_company'),
        (CUSTOMER, "is_customer")
    )
    DICT = dict(CHOICES)
    CODE_DICT = dict(CODES)


class Role(Base):
    """Role Model"""
    name = models.CharField(db_column="Name", max_length=255, unique=True)
    code = models.SlugField(db_column='Code', default='')
    description = models.TextField(null=True, blank=True, db_column="Description")
    access_level = models.IntegerField(db_column="AccessLevel", choices=AccessLevel.CHOICES,
                                       default=AccessLevel.CUSTOMER)

    class Meta:
        db_table = "Role"

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                self.code = slugify(self.name)
            super().save()
        except Exception as e:
            raise

    def get_role_by_code(self=None, code=None):
        try:
            return Role.objects.get(code__exact=code)

        except Exception as e:
            return e


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.user_role = Role.objects.get(code="super_admin")
        user.set_password(password)
        user.is_superuser = False
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_active = True
        user.role = Role.objects.get(code="super_admin")
        user.save()
        return user


class User(AbstractBaseUser, Base, PermissionsMixin):
    """ User model."""
    name = models.CharField(db_column='Name', default="", max_length=255)
    is_active = models.BooleanField(db_column='IsActive', default=True,
                                    help_text='Designates whether this user should be treated as active.')
    email = models.EmailField(unique=True, db_column="Email", help_text="Email Field")
    image = models.ImageField(upload_to='uploads/', db_column="ImageField", null=True, blank=True)
    is_staff = models.BooleanField(default=True,
                                   help_text='Designates whether the user can log into this admin site.')
    user_role = models.ForeignKey(Role, db_column='RoleId', related_name='user_role', on_delete=models.CASCADE,
                                  null=True, blank=True)
    objects = CustomAccountManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'User'

    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                self.email = self.email.replace(" ", "").lower()
            super().save()
        except Exception:
            raise
