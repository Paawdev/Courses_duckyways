import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profile_cv.models import (
    Profile_CV, User_cv, WorkExperience, AcademicEducation, HardSkillUser, SoftSkillUser, LanguageUser,
    CategoryUser, SectorUser, IncorporationUser, Volunteering, Project, Publication, RecognitionAward,
    HardSkill, SoftSkill, Language, Category, Sector, Incorporation, Level
)

faker = Faker()

class Command(BaseCommand):
    help = "Populate the database with fake data"

    def handle(self, *args, **kwargs):
        self.create_users()
        self.create_profiles()
        self.create_user_cvs()
        self.create_work_experiences()
        self.create_academic_educations()
        self.create_hard_skills()
        self.create_soft_skills()
        self.create_languages()
        self.create_categories()
        self.create_sectors()
        self.create_incorporations()
        self.create_volunteerings()
        self.create_projects()
        self.create_publications()
        self.create_recognitions_awards()

    def create_users(self):
        for _ in range(10):  # Cambia este número según cuántos usuarios quieras crear
            User.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                password="password123"
            )

    def create_profiles(self):
        users = User.objects.all()
        for user in users:
            if not Profile_CV.objects.filter(user=user).exists():
                Profile_CV.objects.create(
                    user=user,
                    img_profile=faker.image_url(),
                    img_1_profile=faker.image_url(),
                    img_2_profile=faker.image_url(),
                    img_3_profile=faker.image_url(),
                    img_4_profile=faker.image_url(),
                    address=faker.address(),
                    phone_1=faker.phone_number(),
                    phone_2=faker.phone_number(),
                    email_1=faker.email(),
                    email_2=faker.email(),
                    dni=faker.unique.ssn(),
                    biography=faker.text(),
                    open_to_work=faker.boolean(),
                    vehicle=faker.boolean(),
                    disability=faker.boolean(),
                    disability_percentage=random.randint(0, 100) if faker.boolean() else None
                )

    def create_user_cvs(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            User_cv.objects.create(
                profile_user=profile,
                urlCV=faker.unique.url(),
                template=faker.word(),
                has_img_profile=faker.boolean(),
                has_address=faker.boolean(),
                has_phone_1=faker.boolean(),
                has_phone_2=faker.boolean(),
                has_email_1=faker.boolean(),
                has_email_2=faker.boolean(),
                has_dni=faker.boolean(),
                has_url=faker.boolean(),
                has_biography=faker.boolean(),
                biography=faker.text(),
                has_open_to_work=faker.boolean(),
                has_vehicle=faker.boolean(),
                has_disability=faker.boolean(),
                has_disability_percentage=faker.boolean(),
                has_incorporation=faker.boolean(),
                has_sector=faker.boolean(),
                has_category=faker.boolean(),
                has_work_experiences=faker.boolean(),
                has_hard_skills=faker.boolean(),
                has_soft_skills=faker.boolean(),
                has_languages=faker.boolean(),
                has_academic_educations=faker.boolean(),
                has_volunteerings=faker.boolean(),
                has_projects=faker.boolean(),
                has_publications=faker.boolean(),
                has_recognitions_awards=faker.boolean(),
                has_certifications_courses=faker.boolean()
            )

    def create_work_experiences(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            for _ in range(random.randint(1, 5)):
                WorkExperience.objects.create(
                    profile_user=profile,
                    job_title=faker.job(),
                    start_date=faker.date(),
                    end_date=faker.date(),
                    current_job=faker.boolean(),
                    company_name=faker.company(),
                    description=faker.text(),
                    achievements=faker.text(),
                    references=faker.text(),
                    hard_skills=HardSkillUser.objects.create(
                        profile_user=profile,
                        hard_skill=HardSkill.objects.create(name_hard_skill=faker.word()),
                        description=faker.text(),
                        level_skill=random.randint(1, 5)
                    )
                )

    def create_academic_educations(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            AcademicEducation.objects.create(
                profile_user=profile,
                title=faker.word(),
                academy_name=faker.company(),
                start_date=faker.date(),
                end_date=faker.date(),
                current_education=faker.boolean(),
                references=faker.text()
            )

    def create_hard_skills(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            HardSkillUser.objects.create(
                profile_user=profile,
                hard_skill=HardSkill.objects.create(name_hard_skill=faker.word()),
                description=faker.text(),
                level_skill=random.randint(1, 5)
            )

    def create_soft_skills(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            SoftSkillUser.objects.create(
                profile_user=profile,
                soft_skill=SoftSkill.objects.create(name_soft_skill=faker.word()),
                description=faker.text()
            )

    def create_languages(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            LanguageUser.objects.create(
                profile_user=profile,
                language=Language.objects.create(name_language=faker.word()),
                level=Level.objects.create(name_level=faker.word()),
                certifications=faker.text()
            )

    def create_categories(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            CategoryUser.objects.create(
                profile_user=profile,
                category=Category.objects.create(name_category=faker.word())
            )

    def create_sectors(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            category = Category.objects.create(name_category=faker.word())
            SectorUser.objects.create(
                profile_user=profile,
                sector=Sector.objects.create(name_sector=faker.word(), category=category)
            )

    def create_incorporations(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            IncorporationUser.objects.create(
                profile_user=profile,
                incorporation=Incorporation.objects.create(name_incorporation=faker.word())
            )

    def create_volunteerings(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            Volunteering.objects.create(
                profile_user=profile,
                volunteering_position=faker.job(),
                start_date=faker.date(),
                end_date=faker.date(),
                current_volunteering=faker.boolean(),
                entity_name=faker.company(),
                description=faker.text(),
                achievements=faker.text(),
                references=faker.text()
            )

    def create_projects(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            Project.objects.create(
                profile_user=profile,
                name=faker.word(),
                description=faker.text(),
                link=faker.url()
            )

    def create_publications(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            Publication.objects.create(
                profile_user=profile,
                doi=faker.word(),
                url=faker.url(),
                role=faker.job(),
                name=faker.word()
            )

    def create_recognitions_awards(self):
        profiles = Profile_CV.objects.all()
        for profile in profiles:
            RecognitionAward.objects.create(
                profile_user=profile,
                name=faker.word(),
                entity=faker.company(),
                description=faker.text()
            )