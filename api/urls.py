from django.urls import path, include
from .views import getLocalDATA, helloAPI

urlpatterns = [
    path('hello/', helloAPI),
    path('getLocalData/', getLocalDATA)
]
