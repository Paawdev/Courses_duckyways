from django.urls import path
from . import views

urlpatterns = [
    path('rewards/', views.rewards_list, name="rewards_list"),
    path('redeem/<int:reward_id>/', views.redeem_reward, name="redeem_reward"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('increment-coins/', views.increment_duckycoins, name='increment_duckycoins'),
    path('transactions/', views.transaction_list, name='transaction_list'),

]
