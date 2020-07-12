from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('auth/', authViews.LoginView.as_view(template_name='users/auth.html'), name='auth'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]