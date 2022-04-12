from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('add/', views.addProject_view, name='ajout')
    ]