from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=100)


class Tag(models.Model):
    name = models.CharField(_("name"), max_length=100)


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(_("name"), max_length=100)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, default=0)
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)


