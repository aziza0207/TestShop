from django.contrib import admin
from .models import Product, Category, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["category_id",
                    "name",
                    "price",
                    "description",
                    "created_at"]

    ordering = ["id"]
    search_fields = ["name", "description"]
    list_filter = ["name"]


admin.site.register(Product, ProductAdmin)
