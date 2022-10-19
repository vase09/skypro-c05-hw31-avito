from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from ads.models import Category, Ad
from ads.validators import check_not_published
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    name = serializers.CharField(allow_blank=False, min_length=10, max_length=100)
    price = serializers.IntegerField(min_value=0, default=0)

    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    is_published = serializers.BooleanField(default=None, validators=[check_not_published])

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._author_id = self.initial_data.pop('author_id')
        self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(
                name=validated_data.get('name'),
                price=validated_data.get('price'),
                description=validated_data.get('description'),
                is_published=validated_data.get('is_published')
        )
        ad.author = get_object_or_404(User, pk=self._author_id)
        ad.category = get_object_or_404(Category, pk=self._category_id)
        ad.save()

        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        ad.category = get_object_or_404(Category, pk=self._category_id)
        ad.save()

        return ad


class AdImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
