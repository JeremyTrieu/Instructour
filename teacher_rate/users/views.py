from django.contrib.auth import logout
from django.core.exceptions import ImproperlyConfigured

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .utils import get_and_authenticate_user, create_user_account
from . import serializers

class AuthViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'signin': serializers.UserSignInSerializer,
        'signup': serializers.UserSignUpSerializer,
        'signout': serializers.EmptySerializer,
        'password_change': serializers.PasswordChangeSerializer,
        'password_reset': serializers.PasswordResetSerializer,
        'password_reset_confirm': serializers.PasswordResetConfirmSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def signin(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST', ], detail=False)
    def signout(self, request):
        """
        Calls Django signout method; Does not work for UserTokenAuth.
        """
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST', ], detail=False)
    def password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.get_user_by_email(serializer.data['email'])
        if user:
            services.send_password_reset_mail(user)
        return response.Ok({'message': 'Further instructions will be sent to the email if it exists'})

    @action(methods=['POST', ], detail=False)
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = tokens.get_user_for_password_reset_token(serializer.validated_data['token'])
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return response.NoContent()

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()