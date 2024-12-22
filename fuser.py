import random
from faker import Faker
from django.contrib.auth.models import User, Group

fake = Faker()

def populate_users():
    # Crear o recuperar los grupos
    premium_group, _ = Group.objects.get_or_create(name="premium")
    teacher_group, _ = Group.objects.get_or_create(name="teacher")
    headhunter_group, _ = Group.objects.get_or_create(name="headhunter")

    # Crear 100 usuarios
    users = []
    for _ in range(100):
        first_name = fake.first_name()
        last_name = fake.last_name()
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password("password123")  # Establecer una contraseña predeterminada
        users.append(user)

    # Insertar usuarios en la base de datos en bloque
    User.objects.bulk_create(users)

    # Recuperar los usuarios creados
    all_users = list(User.objects.all())

    # Asignar 10% a premium
    premium_users = random.sample(all_users, k=int(len(all_users) * 0.10))
    for user in premium_users:
        user.groups.add(premium_group)

    # Asignar 5 usuarios a teacher
    teacher_users = random.sample(
        [u for u in all_users if u not in premium_users], k=5
    )
    for user in teacher_users:
        user.groups.add(teacher_group)

    # Asignar 5 usuarios a headhunter
    headhunter_users = random.sample(
        [u for u in all_users if u not in premium_users + teacher_users], k=5
    )
    for user in headhunter_users:
        user.groups.add(headhunter_group)

    print("Usuarios creados y asignados a grupos correctamente.")

if __name__ == "__main__":
    populate_users()
