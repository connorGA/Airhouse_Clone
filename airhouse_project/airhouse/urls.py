from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, LoginView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='airhouse/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='airhouse/logout.html'), name='logout'),
]