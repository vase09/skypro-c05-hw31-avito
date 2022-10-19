from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """Viewset for category model"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
