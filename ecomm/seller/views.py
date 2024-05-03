from django.shortcuts import render
from account.models import products
from rest_framework.viewsets import ViewSet
from .serializer import ProductSerializer



# Create your views here.


class ProductViewSet(ViewSet):
    queryset=products.objects.all()
    serializer_class=ProductSerializer
    