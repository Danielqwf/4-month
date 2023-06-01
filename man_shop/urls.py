from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('product_detail/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product_detail/<int:id>/delete', views.DeleteGoodsView.as_view(), name='delete_goods'),
    path('product_detail/<int:id>/update', views.UpdateProductView.as_view(), name='update_goods'),
    path('add-goods/', views.CreateGoodsView.as_view(), name='create_goods'),
    path('search/', views.Search.as_view(), name='search'),
]

