from rest_framework import serializers
from .models import User, Restaurant, Review


class EachRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'res_name', 'city']


class EachUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'country']


class EachReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_text']


class ListUserReviewSerializer(serializers.ModelSerializer):
    restaurant = EachRestaurantSerializer(read_only = True)
    user = EachUserSerializer(read_only = True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'review_text']
