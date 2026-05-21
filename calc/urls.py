from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history_page, name='history'),
    path('about/', views.about_page, name='about'),
    path('clear/', views.clear_history, name='clear_history'),
]