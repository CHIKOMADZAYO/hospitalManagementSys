from django.urls import path

from .views import CustomLoginView, CustomLogoutView, profile_view, register_view, users_home


urlpatterns = [
    path('', users_home, name='users_home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
]
