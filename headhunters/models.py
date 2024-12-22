from django.db import models
from django.contrib.auth.models import User

from profile_cv.models import Profile_CV, SoftSkill,HardSkill,Sector,Category
from test_management.models import Test




# Model for HeadHunter
# HeadHunter: Este modelo representa a los reclutadores (headhunters) registrados en la plataforma. Cada HeadHunter está vinculado a un usuario (User) de Django mediante una relación uno a uno, lo que permite que el User maneje las credenciales de inicio de sesión mientras HeadHunter almacena información adicional como la compañía, el cargo y los enlaces de contacto profesional.
class HeadHunterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='headhunter')
    company = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100, help_text="Position within the company")
    website = models.URLField(blank=True, null=True, help_text="Company website URL")
    linkedin_profile = models.URLField(blank=True, null=True, help_text="LinkedIn profile URL")
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True,
        help_text="Upload a profile photo"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.company} ({self.position})"

# Model for Profile_CVProfile_CVnd Status (Auxiliary table for Candidate)
#StatusCandidate: Un modelo auxiliar que define posibles estados para los candidatos, como "En proceso", "Contratado", o "Descartado". Estos estados se asignan a los candidatos en el modelo Profile_CV para reflejar su situación general.
class StatusCandidate(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

# Model for Job Offer
#JobOffer: Almacena la información de una oferta de trabajo creada por un HeadHunter, incluyendo el título, descripción y requisitos de la oferta. Cada oferta está relacionada con un HeadHunter específico.
class JobOffer(models.Model):
    headhunter = models.ForeignKey(HeadHunterUser, on_delete=models.CASCADE)  # Headhunter que creó la oferta
    title = models.CharField(max_length=255)  # Título del puesto
    description = models.TextField()  # Descripción del trabajo
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)  # Sector de la oferta
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Categoría del puesto
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True) 
    posted_date = models.DateField(auto_now_add=True) 
    close_date = models.DateField(blank=True, null=True)

    # Relación con habilidades necesarias (puede ser tanto 'hard' como 'soft' skills)
    required_hard_skills = models.ManyToManyField(HardSkill, blank=True, related_name="required_hard_skills")
    required_soft_skills = models.ManyToManyField(SoftSkill, blank=True, related_name="required_soft_skills")

    # Relación con la experiencia requerida para el puesto
    required_experience = models.IntegerField(blank=True, null=True)
    
    #Agreagando mas de un test a la oferta si el headhunter quiere, no es necesario 
    JobOfferTests = models.ManyToManyField(Test, blank=True, related_name="job_offers")

    def __str__(self):
        return self.title


# Model for Management of Candidates in Job Offers

# ManagementCandidates: Este modelo gestiona la relación entre un Profile_CV y una JobOffer, permitiendo que cada oferta tenga múltiples candidatos asociados. Los campos is_selected_by_headhunter y applied_directly permiten identificar si un candidato fue seleccionado por el headhunter o si aplicó a la oferta por cuenta propia. Además, este modelo incluye un campo status para registrar el estado de ese candidato en la oferta específica, lo que puede diferir del estado general del candidato.

class ManagementCandidates(models.Model):
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Profile_CV, on_delete=models.CASCADE)
    is_selected_by_headhunter = models.BooleanField(
        default=False,
        help_text="Indicates if the candidate was selected directly by the headhunter"
    )
    applied_directly = models.BooleanField(
        default=False,
        help_text="Indicates if the candidate applied to the job offer by themselves"
    )
    status = models.ForeignKey(StatusCandidate, on_delete=models.SET_NULL, null=True)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        selected_or_applied = "Selected" if self.is_selected_by_headhunter else "Applied Directly"
        return f"{self.candidate.name} - {self.job_offer.title} ({selected_or_applied})"

# Model for Status Action (Auxiliary table for Action)
#StatusAction: Define los posibles estados para las acciones realizadas por el headhunter en relación con un candidato (por ejemplo, "Enviado", "En proceso", "Finalizado"). Este modelo auxiliar proporciona opciones de estado para el modelo Action.
class StatusAction(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Model for Type of Action
#Tabla Auxiliar de Action
class TypeAction(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Model for Actions taken by the headhunter on candidates
#Action: Almacena las acciones o interacciones realizadas por el headhunter con un candidato, como enviar un mensaje, realizar una videoconferencia o enviar un email. Cada Action está relacionada con un HeadHunter y un CandidateProfile y tiene un tipo de acción (type_action), una descripción y una fecha.
class Schedule(models.Model):
    headhunter = models.ForeignKey(HeadHunterUser, on_delete=models.CASCADE)
    joboffer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Profile_CV, on_delete=models.CASCADE)
    type_action = models.ForeignKey(TypeAction, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    status = models.ForeignKey(StatusAction, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.type_action.name} with {self.candidate.name} - {self.date}"

# Model for Job Offer Notification
#JobOfferNotification: Registra notificaciones enviadas a los candidatos sobre una oferta de trabajo, incluyendo la fecha en que se envió y si el candidato ha leído la notificación o no. Esto es útil para mantener informados a los candidatos sobre el progreso de sus aplicaciones.
class JobOfferNotification(models.Model):
    candidate = models.ForeignKey(Profile_CV, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.job_offer.title} to {self.candidate.name}"
