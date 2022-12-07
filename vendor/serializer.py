from rest_framework import serializers

from vendor.models import Buyer
from vendor.models import Seller
from vendor.models import Products
from vendor import services
# BUYER SERIALIZER
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

# SELLER SERIALIZER
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return services.UserDataClass(**data)

# PRODUCTS SERIALIZER
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
# USER SERIALIZER
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return response.Response(data={data})
# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         fields = ('id', 'name', 'codename')

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'name')

# class AuthUserSerializer(serializers.ModelSerializer):

#     groups = GroupSerializer(many=True) 
#     permissions = PermissionSerializer(many=True, source='user_permissions')

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email', 
#             'is_staff', 'is_active', 'is_superuser', 'last_login', 
#             'date_joined', 'groups', 'user_permissions', 'permissions')