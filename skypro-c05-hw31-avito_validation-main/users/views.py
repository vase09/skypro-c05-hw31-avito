from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView

from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer


class UserListView(ListAPIView):
    """Show all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    """Show user by id"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    """Create user"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """Update user by id"""
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    """Delete user by id"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
