from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostPossessor
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

# Create your views here.


class ListCategory(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListBook(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['price']


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListProduct(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    filter_backends = [OrderingFilter]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ordering_fields = ['price']


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

