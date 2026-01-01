from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nha-gai/', views.bride_side, name='bride_side'),
]
