from rest_framework import serializers

from vendor.models import Buyer
from vendor.models import Seller
from vendor.models import Products

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data