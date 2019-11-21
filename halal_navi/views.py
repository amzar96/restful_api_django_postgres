from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Restaurant, Review
from .serializers import (
    EachRestaurantSerializer,
    EachReviewSerializer,
    EachUserSerializer,
    ListUserReviewSerializer,
)
from itertools import chain


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = EachRestaurantSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EachUserSerializer


class ListReviewBasedUser(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ListUserReviewSerializer

