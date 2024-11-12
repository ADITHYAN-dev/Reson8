from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search-history/', views.search_history, name='search_history'),
    
]
