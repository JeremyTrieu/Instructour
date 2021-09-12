from uuid import UUID
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user

def create_user_account(
        email, 
        password, 
        full_name="",
        **kwargs
    ):
    return get_user_model().objects.create_user(
        email=email, 
        password=password, 
        full_name=full_name
    )

def get_user_by_email(email: str):
    return get_user_model().objects.filter(email__iexact=email).first()