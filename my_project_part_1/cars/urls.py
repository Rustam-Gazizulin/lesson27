from django.urls import path
from cars import views

urlpatterns = [
    path('', views.list_car, name='list_cars'),
    path('<int:pk>/', views.get_car, name='car'),
    path('search/', views.search, name='search_brand'),
]
