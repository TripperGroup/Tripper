from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):  # pylint: disable=function-redefined
    class Meta(UserCreateSerializer):
        model = User
        fields = '__all__'
