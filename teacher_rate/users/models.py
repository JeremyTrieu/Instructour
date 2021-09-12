from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField, PPOIField

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, full_name, password=None, is_staff = False, is_admin=False, is_superuser=False, is_active = True, **kwargs):
        if not email:
            raise ValueError(_("Email address is required!"))
        if not password:
            raise ValueError(_("Password is required!"))
        if not full_name:
            raise ValueError(_("Full Name is required!"))

        user = self.model(
            email = self.normalize_email(email),
            full_name=full_name,
            **kwargs
        )
        user.set_password(password)
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, full_name, password=None, **kwargs):
        return self.create_user(
            email = self.normalize_email(email),
            full_name= full_name,
            password=password,
            is_staff=True,
            **kwargs
        )

    def create_superuser(self, email, full_name, password=None, **kwargs):
        return self.create_user(
            email = self.normalize_email(email),
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
            **kwargs
        )

class CustomUser(AbstractBaseUser):
    username = None
    email           = models.EmailField(_('email'), unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True) 

    full_name       = models.CharField(verbose_name='Full Name', max_length=255, blank=True, null=False)

    admin        = models.BooleanField(default=False)
    active       = models.BooleanField(default=True)
    staff        = models.BooleanField(default=False)
    superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()


    def __str__(self):
        return self.full_name


    def get_full_name(self) -> str:
        return f"{self.email} - {self.full_name}"


    @property
    def is_staff(self):
        return self.staff


    @property
    def is_admin(self):
        return self.admin


    @property
    def is_active(self):
        return self.active


    @property
    def is_superuser(self):
        return self.superuser


    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ManyToManyField(Image, related_name='profile')

    def __str__(self):
        return self.full_name
