from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form_view, name='form'),
    path('show/', views.show_data, name='show'),
]

