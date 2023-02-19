from rest_framework.views import Response
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from account.api.selectors import user_list
from account.api.serializers import (
    UserReadSerializer, 
    UserCreateSerializer, 
    UserUpdateSerializer,
    ChangePasswordSerializer
)
from account.api.filters import UserFilter
from account.api.services import create_user, update_user

class UserViewSet(viewsets.ModelViewSet):
    queryset = user_list()
    serializer_class = UserReadSerializer
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'update':
            return UserUpdateSerializer
        
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_user(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_user(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    
    @action(methods=["GET"], detail=False)
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    @action(methods=["POST"], detail=False, serializer_class=ChangePasswordSerializer, url_path="change-password")
    def change_password(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.data.get("old_password")):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.data.get("new_password"))
        user.save()
        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'detail': 'Password updated successfully',
            'data': []
        }

        return Response(response)

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)