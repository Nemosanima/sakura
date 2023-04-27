from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_system, name='login'),
    path('logout/', views.logout_system, name='logout'),
    path('signup/', views.signup_system, name='signup'),
]
