from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    slug = models.SlugField(null=True, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
