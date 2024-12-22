import os
import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from headhunters.models import (
    HeadHunterUser, JobOffer, ManagementCandidates, StatusCandidate,
    StatusAction, TypeAction, Schedule, JobOfferNotification
)
from profile_cv.models import Profile_CV, WorkExperience


class Command(BaseCommand):
    help = "Popula la base de datos con datos falsos para pruebas."

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Funciones de creación
        def create_users_and_headhunters(n=10):
            for _ in range(n):
                username = faker.user_name()
                user = User.objects.create_user(
                    username=username,
                    email=faker.email(),
                    password='password123'
                )
                HeadHunterUser.objects.create(
                    user=user,
                    company=faker.company(),
                    phone=faker.phone_number(),
                    position=faker.job(),
                    website=faker.url(),
                    linkedin_profile=faker.url(),
                    city=faker.city(),
                    country=faker.country(),
                    profile_photo=None
                )
            print(f"Creados {n} usuarios y headhunters.")

        def create_status_and_actions():
            status_candidates = ['En proceso', 'Contratado', 'Descartado']
            status_actions = ['Enviado', 'En proceso', 'Finalizado']
            action_types = ['Entrevista', 'Email', 'Llamada', 'Videoconferencia']

            for status in status_candidates:
                StatusCandidate.objects.get_or_create(name=status)

            for status in status_actions:
                StatusAction.objects.get_or_create(name=status)

            for action in action_types:
                TypeAction.objects.get_or_create(name=action)

            print("Estados de candidatos y acciones creados.")

        # Llama a las funciones aquí
        create_users_and_headhunters()
        create_status_and_actions()
        # Puedes agregar más llamadas a las demás funciones según tu script original.
        print("¡Población de datos completada!")
