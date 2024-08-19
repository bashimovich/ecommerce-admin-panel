from rest_framework import serializers
from django.contrib.auth.models import User
from shop.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["add", "is_main"]


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)

    class Meta:
        model = User
        fields = ("username", "address",)
