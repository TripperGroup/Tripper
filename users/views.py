from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, FollowingSerializer, UserSummerySerializer
from .models import User, UserFollowing
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,request

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserSummeryViewSet(viewsets.ModelViewSet):
    serializer_class = UserSummerySerializer
    queryset = User.objects.all()

class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = FollowingSerializer
    queryset = UserFollowing.objects.all()

class FollowerViewSet(viewsets.ModelViewSet):
    serializer_class = FollowingSerializer
    queryset = UserFollowing.objects.all()
    # user = User.objects.get(id=2)
    # queryset = user.followers.all()
    