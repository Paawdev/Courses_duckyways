from django.urls import path
from .views import teacher_dashboard,dashboard, teacher_chat, headhunter_dashboard, headhunter_chat, premium_chat,premium_dashboard, premium_profile

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher_chat/', teacher_chat, name='teacher_chat'),
    path('headhunter_dashboard/', headhunter_dashboard, name='headhunter_dashboard'),
    path('headhunter_chat/', headhunter_chat, name='headhunter_chat'),
    path('premium_dashboard/', premium_dashboard, name='premium_dashboard'),
    path('premium_chat/', premium_chat, name='premium_chat'),
    path('premium_profile/', premium_profile, name='premium_profile'),

 
    
]
