from django.shortcuts import get_object_or_404
from .serializers import ArticleSerializer
from .models import Article
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,request

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

