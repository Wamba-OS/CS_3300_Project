from django.urls import path
from . import views

urlpatterns = [
    path('amazon/', views.produce_query, name='WOW!')
]

