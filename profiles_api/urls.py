from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
"""You only need a base_name when you don't have a query set or you want you
override the name of the query set associated to it"""
router.register('hello-viewset',views.HelloViewSet,base_name ='hello-viewset' )
router.register('profile-viewset',views.UserProfileViewSet)
urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
