from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restaurant', views.RestaurantView)
router.register('user', views.UserView)
router.register('review', views.ListReviewBasedUser)

urlpatterns = [
    path(r'', include(router.urls))
]