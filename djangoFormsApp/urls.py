from django.urls import path
from .views import landing, dashboard, register, login, logout, createDragon

urlpatterns = [
    path('', landing, name='landing'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('dragon/create', createDragon),
    
]
