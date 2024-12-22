from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DuckyCoin)
admin.site.register(Badge)
admin.site.register(Reward)
admin.site.register(DuckyCoinTransaction)
