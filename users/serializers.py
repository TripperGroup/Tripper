from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):  # pylint: disable=function-redefined
    class Meta(UserCreateSerializer):
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = User
        fields = '__all__'

class UserSummerySerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = User
        fields = ('username','avatar' )


class FollowingSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = UserFollowing
        fields = ('user_id','following_user_id')
        