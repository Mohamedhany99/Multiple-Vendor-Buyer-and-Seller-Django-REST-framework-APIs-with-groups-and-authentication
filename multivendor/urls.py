"""multivendor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

import vendor.api_views
urlpatterns = [
    path('api/',include("vendor.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('buyer/',vendor.api_views.BuyerList.as_view()),
    path('buyer/create/',vendor.api_views.BuyerCreate.as_view()),
    path('buyer/<int:id>/',vendor.api_views.BuyerList.as_view()),
    
    path('seller/',vendor.api_views.SellerList.as_view()),
    path('seller/create/',vendor.api_views.SellerCreate.as_view()),
    path('seller/<int:id>/',vendor.api_views.SellerRetrieveUpdateDestroy.as_view()),

    
    path('products/',vendor.api_views.ProductsList.as_view()),
    path('products/create/',vendor.api_views.ProductsCreate.as_view()),
    path('products/<int:id>/',vendor.api_views.ProductsRetrieveUpdateDestroy.as_view()),
]

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()