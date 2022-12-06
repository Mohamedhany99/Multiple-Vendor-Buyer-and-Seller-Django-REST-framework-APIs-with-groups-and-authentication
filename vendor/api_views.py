from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import permissions

from vendor.models import Buyer
from vendor.models import Seller
from vendor.models import Products
from vendor.serializer import BuyerSerializer
from vendor.serializer import SellerSerializer
from vendor.serializer import ProductsSerializer


class AllPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
    
# Buyer Functions
class BuyerList(ListAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name')
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticated]
class BuyerCreate(CreateAPIView):
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        # try:
        #     passvalidate =  request.data.get('category')
        #     if price is not None and float(price) <= 0.0:
        #         raise ValidationError({ 'price': 'Must be above $0.00' })
        # except ValueError:
        #     raise ValidationError({ 'price': 'A valid number is required' })
        
        # print("request = ",request.data.get('category'))
        return super().create(request, *args, **kwargs)

class BuyerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    lookup_field = 'id'
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        item_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('item_data_{}'.format(item_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            item = response.data
            cache.set('item_data_{}'.format(item['id']), {
                'name': item['name'],
            })
        return response

# seller functions
class SellerList(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name')
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticated]

class SellerCreate(CreateAPIView):
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        # try:
        #     passvalidate =  request.data.get('category')
        #     if price is not None and float(price) <= 0.0:
        #         raise ValidationError({ 'price': 'Must be above $0.00' })
        # except ValueError:
        #     raise ValidationError({ 'price': 'A valid number is required' })
        
        print("request = ",request.data.get('category'))
        return super().create(request, *args, **kwargs)

class SellerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    lookup_field = 'id'
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        item_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('item_data_{}'.format(item_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            item = response.data
            cache.set('item_data_{}'.format(item['id']), {
                'name': item['name'],
            })
        return response

# Products Functions
class ProductsList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name')
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticated]

class ProductsCreate(CreateAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        # try:
        #     passvalidate =  request.data.get('category')
        #     if price is not None and float(price) <= 0.0:
        #         raise ValidationError({ 'price': 'Must be above $0.00' })
        # except ValueError:
        #     raise ValidationError({ 'price': 'A valid number is required' })
        
        print("request = ",request.data.get('category'))
        return super().create(request, *args, **kwargs)

class ProductsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    lookup_field = 'id'
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        
        item_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('item_data_{}'.format(item_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            item = response.data
            cache.set('item_data_{}'.format(item['id']), {
                'name': item['name'],
                'price': item['price'],
            })
        return response