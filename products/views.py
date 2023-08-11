from datetime import datetime
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductListSerializer
from .models import Product
from django.core.cache import cache
import xlwt


class ProductListView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated, )
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = cache.get('queryset')

        if queryset is None:
            queryset = Product.objects.all()
            cache.set('queryset', queryset)

        return queryset


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Products')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["Id",
               "Category",
               "Tags",
               "Name",
               "Price",
               "Description",
               "Created_at"]

    for column in range(len(columns)):
        ws.write(row_num, column, columns[column], font_style)

    font_style = xlwt.XFStyle()
    rows = Product.objects.all() \
        .values_list("id",
                     "category",
                     "tags",
                     "name",
                     "price",
                     "description",
                     "created_at")
    for row in rows:
        row_num += 1
        for column in range(len(row)):
            ws.write(row_num, column, str(row[column]), font_style)
    wb.save(response)
    return response
