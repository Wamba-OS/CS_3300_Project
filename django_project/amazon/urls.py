from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('search/', views.user_search, name='WOW!')
]

