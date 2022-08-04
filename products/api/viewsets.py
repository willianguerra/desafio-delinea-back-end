from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from products.api import serializers
from products import models


class ProductsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()
