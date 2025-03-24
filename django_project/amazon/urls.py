from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('search/', views.get_search, name='get_search'),
    path('results/', views.results, name='results'),
]

