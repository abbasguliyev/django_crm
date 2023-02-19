from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'last_login']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'groups', 'user_permissions', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
