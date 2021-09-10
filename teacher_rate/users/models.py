from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin = False, is_active = True):
        if not email:
            raise ValueError("Email address is required!")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    first_name = models.CharField('First Name', max_length=255, blank=True,
                                null=False)

    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                null=False)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"


    def get_full_name(self) -> str:
        return f"{self.email} - {self.first_name} {self.last_name}"


    def get_short_name(self) -> str:
        return f"{self.email} - {self.first_name} {self.last_name}"


    @property
    def is_staff(self):
        return self.staff


    @property
    def is_admin(self):
        return self.admin


    @property
    def is_active(self):
        return self.active

    