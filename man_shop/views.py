from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def product_view(request):
    products = models.Shop.objects.all()
    return render(request, 'shop/shop.html', {'products': products})


def product_detail_view(request, id):
    product_id = get_object_or_404(models.Shop, id=id)
    return render(request, 'shop/shop_detail.html', {'product_id': product_id})


def create_goods_view(request):
    '''добавление'''
    method = request.method
    if method == 'POST':
        form = forms.ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Товар успешно добавлен.')
    else:
        form = forms.ShopForm()
    return render(request, 'crud/create_goods.html', {'form': form})


def delete_goods_view(request, id):
    '''удаление'''
    goods_id = get_object_or_404(models.Shop, id=id)
    goods_id.delete()
    return HttpResponse('товар удалён')


def update_product_view(request, id):
    '''Обновление'''
    product_id = get_object_or_404(models.Shop, id=id)
    if request.method == 'POST':
        form = forms.ShopForm(instance=product_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные обновлены')
    else:
        form = forms.ShopForm(instance=product_id)
    context = {
        'form': form,
        'product_id': product_id
    }
    return render(request, 'crud/update_goods.html', context)
