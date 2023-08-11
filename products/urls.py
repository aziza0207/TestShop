from django.urls import path
from .views import ProductListView, export_excel


urlpatterns = [path('product/', ProductListView.as_view(), name='product'),
               path('export-excel', export_excel)]
