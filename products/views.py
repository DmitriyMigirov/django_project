import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, TemplateView

from products.forms import ImportForm
from products.models import Product
from onlinestore.mixins.views_mixins import StaffUserCheck
from django.conf import settings




class ProductView(ListView):
    model = Product

    def get_queryset(self):
        return self.model.get_products()



class ProductDetail(DetailView):
    model = Product


@login_required
def export_csv(request, *args, **kwargs):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="products.csv"'}
    )
    fieldnames = ['name', 'category', 'description', 'price', 'sku', 'image']
    writer = csv.DiscWriter(response, fieldnames=fieldnames)


    writer.writeheader()
    for product in Product.objects.iterator():
        writer.writerow({
            'name' : product.name,
            'category' : product.category.name,
            'description' : product.description,
            'price' : product.price,
            'sku' : product.sku,
            'image' : settings.DOMAIN + product.image.url
        })
    return response


class ImportCSVIntoProducts(StaffUserCheck, FormView):
    template_name = 'products/import_csv.html'
    form_class = ImportForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
