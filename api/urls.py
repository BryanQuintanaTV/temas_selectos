from django.urls import path
from .views import ItemList, ItemReport

urlpatterns = [
    path('api/v1/chat/', ItemList.as_view(), name='item-list'),
    path('api/v1/report/', ItemReport.as_view(), name='item-report'),
]