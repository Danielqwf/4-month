from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


# Не полная информация
class ProductView(generic.ListView):
    template_name = 'shop/shop.html'
    queryset = models.Shop.objects.all()

    def get_queryset(self):
        return models.Shop.objects.all()

# def product_view(request):
#     products = models.Shop.objects.all()
#     return render(request, 'shop/shop.html', {'products': products})

# Детальная информация
class ProductDetailView(generic.DetailView):
    template_name = 'shop/shop_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=product_id)

# def product_detail_view(request, id):
#     product_id = get_object_or_404(models.Shop, id=id)
#     return render(request, 'shop/shop_detail.html', {'product_id': product_id})


# Добваление товара
class CreateGoodsView(generic.CreateView):
    template_name = 'crud/create_goods.html'
    form_class = forms.ShopForm
    queryset = models.Shop.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateGoodsView, self).form_valid(form=form)

# def create_goods_view(request):
#     '''добавление'''
#     method = request.method
#     if method == 'POST':
#         form = forms.ShopForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Товар успешно добавлен.')
#     else:
#         form = forms.ShopForm()
#     return render(request, 'crud/create_goods.html', {'form': form})

# Удаление товара
class DeleteGoodsView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=product_id)

# def delete_goods_view(request, id):
#     '''удаление'''
#     goods_id = get_object_or_404(models.Shop, id=id)
#     goods_id.delete()
#     return HttpResponse('товар удалён')


# Обновление
class UpdateProductView(generic.UpdateView):
    template_name = 'crud/update_goods.html'
    form_class = forms.ShopForm
    success_url = '/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=product_id)

    def form_valid(self, form):
        return super(UpdateProductView, self).form_valid(form=form)

# def update_product_view(request, id):
#     '''Обновление'''
#     product_id = get_object_or_404(models.Shop, id=id)
#     if request.method == 'POST':
#         form = forms.ShopForm(instance=product_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Данные обновлены')
#     else:
#         form = forms.ShopForm(instance=product_id)
#     context = {
#         'form': form,
#         'product_id': product_id
#     }
#     return render(request, 'crud/update_goods.html', context)



class Search(generic.ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_queryset(self):
        return models.Shop.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
