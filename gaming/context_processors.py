from gaming.models import DuckyCoin

def user_duckycoins(request):
    if request.user.is_authenticated:
        try:
            return {'user_duckycoins': request.user.duckycoins.balance}
        except DuckyCoin.DoesNotExist:
            return {'user_duckycoins': 0}
    return {'user_duckycoins': None}
