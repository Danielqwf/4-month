from django.shortcuts import render, get_object_or_404
from . import models

def product_view(request):
    products = models.Shop.objects.all()
    return render(request, 'shop/shop.html', {'products': products})


def product_detail_view(request, id):
    product_id = get_object_or_404(models.Shop, id=id)
    return render(request, 'shop/shop_detail.html', {'product_id': product_id})
