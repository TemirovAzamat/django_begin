from django.urls import path

from . import views

urlpatterns = [
    path('shop/', views.list_item, name='item'),
    path('shop/<int:item_id>/', views.detail_item, name='detail'),
]

