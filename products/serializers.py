from rest_framework import serializers
from .models import Product, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


def get_tags(obj):
    return [tag.name for tag in obj.tags.all()]


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
