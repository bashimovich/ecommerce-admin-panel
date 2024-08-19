from rest_framework import viewsets
from shop.models import Cart, Address, Order, OrderProducts
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UsersViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
