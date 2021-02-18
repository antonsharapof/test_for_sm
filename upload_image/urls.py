from django.urls import path
from .views import first_way, SecondWay

urlpatterns = [
    path('first/', first_way),
    path('second/', SecondWay.as_view({'post': 'create'}))
]
