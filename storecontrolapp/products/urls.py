from django.urls import path

from products import views

urlpatterns = [
  path('', views.product_list, name='product_list'),
  path('view/<int:pk>', views.product_view, name='product_view'),
  path('new', views.product_create, name='product_new'),
  path('edit/<int:pk>', views.product_update, name='product_edit'),
  path('delete/<int:pk>', views.product_delete, name='product_delete'),
]