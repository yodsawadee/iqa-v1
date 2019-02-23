from django.urls import path, include
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name = 'inbox'),
]