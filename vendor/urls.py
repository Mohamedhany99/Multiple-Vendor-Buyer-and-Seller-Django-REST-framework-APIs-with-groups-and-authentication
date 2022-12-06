from django.contrib import admin
from django.urls import path , include

import vendor.api_views
urlpatterns = [
    path('register/',vendor.api_views.RegisterAPI.as_view(),name="register"),
]