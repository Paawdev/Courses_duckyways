from django.shortcuts import render, get_object_or_404, redirect
from .models import Reward
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import DuckyCoin, DuckyCoinTransaction

#http://127.0.0.1:8000/gaming/increment-coins/?amount=10&reason=Completed%20profile

@login_required
def transaction_list(request):
    transactions = DuckyCoinTransaction.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'gaming/transaction_list.html', {'transactions': transactions})

@login_required
def increment_duckycoins(request):
    # Obtener los parámetros de la solicitud
    amount = int(request.GET.get('amount', 0))  # Valor pasado como parámetro (?amount=10)
    reason = request.GET.get('reason', 'No reason provided')  # Explicación (?reason=Completed profile)

    # Obtener el registro de DuckyCoin del usuario
    duckycoin, created = DuckyCoin.objects.get_or_create(user=request.user)

    # Incrementar los puntos
    duckycoin.balance += amount
    duckycoin.save()

    # Responder con un JSON (o redirigir según necesites)
    return JsonResponse({
        'message': 'DuckyCoins incrementados correctamente.',
        'new_balance': duckycoin.balance,
        'reason': reason,
        'amount_added': amount
    })


def rewards_list(request):
    rewards = Reward.objects.all()
    return render(request, "gaming/rewards_list.html", {"rewards": rewards})

def redeem_reward(request, reward_id):
    reward = get_object_or_404(Reward, id=reward_id)
    user_coins = request.user.duckycoins

    if reward.stock > 0 and user_coins.remove_coins(reward.cost):
        reward.stock -= 1
        reward.save()
        return render(request, "gaming/redeem_success.html", {"reward": reward})
    else:
        return render(request, "gaming/redeem_fail.html")


from .models import DuckyCoin

def leaderboard(request):
    top_users = DuckyCoin.objects.order_by('-balance')[:10]
    return render(request, "gaming/leaderboard.html", {"top_users": top_users})
