from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_inventory, name='view_inventory'),
    path('inventory/add/', views.add_item_to_inventory, name='add_item_to_inventory'),
]
