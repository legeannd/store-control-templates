from django.urls import path

from products import views

urlpatterns = [
  path('', views.product_list, name='product_list'),
  path('new', views.product_create, name='product_new'),
  path('edit/<int:pk>', views.product_update, name='product_edit'),
  path('edit/', views.product_list, name='product_edit_no_id'),
  path('delete/<int:pk>', views.product_delete, name='product_delete'),
  path('delete/', views.product_list, name='product_delete_no_id'),
]