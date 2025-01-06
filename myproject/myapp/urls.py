from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, weather_page, post_list

urlpatterns = [
    path('', post_list, name='post_list'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('weather/', weather_page, name='weather_page'),
]
