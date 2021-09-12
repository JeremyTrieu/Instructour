from rest_framework import exceptions
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model, password_validation
from versatileimagefield.serializers import VersatileImageFieldSerializer


User = get_user_model()


class EmptySerializer(serializers.Serializer):
    pass


class UserSignInSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSignUpSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """

    password2 = serializers.CharField(style={'input_type':'password'}, write_only = True, required=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'password', 'password2')
        extra_kwargs = {
            'email':{'required':True},
            'password':{'write_only':True}
        }
    
    # Link: https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    # Validate password
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        errors = {}
        if not password2:
            errors['password2'] = "Please re-enter a password to confirm"
        if password != password2:
            errors['password2'] = "Passwords don't match!"

        try:
            # validate the password and catch the exception
            password_validation.validate_password(password=password)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        try:
            password_validation.validate_password(password=password2)

        except exceptions.ValidationError as e:
            errors['password2'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSignUpSerializer, self).validate(data)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_admin', 'is_superuser')
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def get_auth_token(self, sender, instance=None, created=False, **kwargs):
        """ When a user is created create an authorization token for them"""
        if created:
            token = Token.objects.create(user=instance)
            print("Token created for new user!")
            return token.key


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value


    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)


    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

# class ImageSerializer(FlexFieldsModelSerializer):
#     image = VersatileImageFieldSerializer(
#         sizes=[
#             ('full_size', 'url'),
#             ('thumbnail', 'thumbnail__100x100'),
#         ]
#     )

#     class Meta:
#         model = Image
#         fields = ['pk', 'name', 'image']