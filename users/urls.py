from django.urls import path
from .views import home, profile, RegisterView
from django.views.generic import TemplateView


app_name="users"

urlpatterns = [
    path('', home, name='users-home'),
    
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
