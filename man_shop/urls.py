from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name='products'),
    path('product_detail/<int:id>/', views.product_detail_view, name='product_detail')
]
