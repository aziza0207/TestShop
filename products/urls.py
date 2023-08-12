from django.urls import path
from .views import ProductListView, ExportExcelView


urlpatterns = [path('product/', ProductListView.as_view(), name='product'),
               path('export-excel', ExportExcelView.as_view())]
