from django.urls import path
from . import views

urlpatterns = [
    path('amazon/', views.amaze, name='WOW!')
]