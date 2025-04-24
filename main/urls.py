from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.survey_form, name='form'),
    path('success/', views.success, name='success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]