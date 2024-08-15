from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('forget-password/', views.forgotPassword, name='forget_password'),
    path('password-reset-sent/<str:reset_id>/', views.passwordResetSent, name='password_reset_sent'),
    path('reset-password/<str:reset_id>/', views.resetPassword, name='reset_password'),
]