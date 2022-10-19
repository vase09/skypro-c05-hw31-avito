from rest_framework import serializers

from ads.models import Category


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(min_length=5, max_length=10)

    class Meta:
        model = Category
        fields = '__all__'
