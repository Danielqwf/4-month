from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_view, name='products'),
    path('product_detail/<int:id>/', views.product_detail_view, name='product_detail'),
    path('product_detail/<int:id>/delete', views.delete_goods_view, name='delete_goods'),
    path('product_detail/<int:id>/update', views.update_product_view, name='update_goods'),
    path('add-goods/', views.create_goods_view, name='create_goods'),
]

