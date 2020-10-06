from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('search/', views.SearchView.as_view(), name='search'),
]