from django.urls import path
from .views import ItemList

urlpatterns = [
    path('api/v1/chat/', ItemList.as_view(), name='item-list'),
]