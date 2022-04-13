from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index_view),
    path('add/', views.addProject_view, name='ajout'),
    path('history/', views.history_view, name='history'),
    path('accounts/login/', auth_view.LoginView.as_view(), name='login'),
    path('allprojects/', views.allProject_views, name='allProjects'),
    path('<int:project_id>/edit/', views.update_view, name='update')
    ]