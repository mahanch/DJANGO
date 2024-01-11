from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, DetailView


# Create your views here.

class ProductListView(ListView):
    template_name = 'product/product_lists.html'
    model = models.Products
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


# def product_lists(request):
#     list_product = models.Products.objects.all().order_by('-price')[:5]
#     return render(request, 'product/product_lists.html', {
#         "products": list_product
#     })


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = models.Products


# def product_detail(request, slug):
#     get_object = get_object_or_404(models.Products, slug=slug)
#     return render(request, 'product/product_detail.html', {
#         "product": get_object
#     })
