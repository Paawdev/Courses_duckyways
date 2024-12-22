from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class DuckyCoinTransaction(models.Model):
    ACTION_TYPES = [
        ('increment', 'Incremento'),
        ('decrement', 'Decremento'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="duckycoin_transactions")
    action_type = models.CharField(max_length=10, choices=ACTION_TYPES)
    timestamp = models.DateTimeField(default=now)
    application = models.CharField(max_length=100, help_text="Nombre de la aplicación que registró la acción")
    description = models.TextField(help_text="Descripción de la acción realizada")
    amount = models.IntegerField(help_text="Cantidad de DuckyCoins afectados")

    def __str__(self):
        return f"{self.user.username} - {self.action_type} {self.amount} DuckyCoins - {self.timestamp}"

# Modelo DuckyCoin
class DuckyCoin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="duckycoins")
    balance = models.IntegerField(default=0)

    def add_coins(self, amount, application, description):
        self.balance += amount
        self.save()

        # Registrar la transacción
        DuckyCoinTransaction.objects.create(
            user=self.user,
            action_type='increment',
            application=application,
            description=description,
            amount=amount
        )

    def remove_coins(self, amount, application, description):
        if self.balance >= amount:
            self.balance -= amount
            self.save()

            # Registrar la transacción
            DuckyCoinTransaction.objects.create(
                user=self.user,
                action_type='decrement',
                application=application,
                description=description,
                amount=amount
            )
            return True
        return False


# Modelo Badge
class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to="badges/")
    users = models.ManyToManyField(User, related_name="badges", blank=True)

    def __str__(self):
        return self.name

# Modelo Reward
class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
    icon = models.ImageField(upload_to="rewards/")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
