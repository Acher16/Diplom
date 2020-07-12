from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ref-home'),
    path('ref/', views.RefCreate.as_view(), name='ref'),
]