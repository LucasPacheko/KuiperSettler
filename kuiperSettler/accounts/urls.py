from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_handle, name='login'),
    path('logout/', views.logout_handle, name='logout'),
]
