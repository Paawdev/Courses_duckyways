from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('message/<int:pk>/', views.view_message, name='view_message'),
    path('send/', views.send_message, name='send_message'),
    path('search_users/', views.search_users, name='search_users'),
    path('deactivate_message/<int:pk>/', views.deactivate_message, name='deactivate_message'),
    path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),
    path('reactivate_message/<int:pk>/', views.reactivate_message, name='reactivate_message'),

]
