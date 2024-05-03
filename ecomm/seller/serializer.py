from rest_framework import serializers
from account.models import products
# from django.contrib.auth.models import User

# class ProductSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     description=serializers.CharField()
#     price=serializers.IntegerField()
#     image=serializers.ImageField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields="all"