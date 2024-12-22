from django import forms
from test_management.models import Test
from profile_cv.models import Profile_CV, Sector, Category
from .models import HeadHunterUser, JobOffer, ManagementCandidates, Schedule, JobOfferNotification
class HeadHunterForm(forms.ModelForm):
    class Meta:
        model = HeadHunterUser
        #Se agrega el campo user, para probar la creacion de headhunter y la vista de detalle, luego con el manejo de login se eliminara
        
        fields = [
            'user','company', 'phone', 'position', 'website',
            'linkedin_profile', 'city', 'country', 'profile_photo'
        ]
        labels = {
            'usuario' : 'Usuario',
            'company': 'Nombre de la empresa',
            'phone': 'Teléfono',
            'position': 'Cargo',
            'website': 'Sitio Web',
            'linkedin_profile': 'Perfil de LinkedIn',
            'city': 'Ciudad',
            'country': 'País',
            'profile_photo': 'Foto de Perfil',
        }

        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Idonium'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recursos Humanos'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'linkedin_profile': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn URL'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Barcelona'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'España'}),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_CV
        fields = '__all__'

from django import forms

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        exclude = ['headhunter']
        fields = [
            'headhunter','title', 'description', 'sector', 'category', 
            'salary', 'location', 'close_date', 
            'required_hard_skills', 'required_soft_skills', 
            'required_experience', 'JobOfferTests'
        ]
        sector = forms.ModelChoiceField(
        queryset=Sector.objects.all(),  # Obtiene todos los sectores
        widget=forms.Select(attrs={'class': 'form-control'}),  # Estilo de Bootstrap para el <select>
        required=True  # Asegúrate de que este campo sea obligatorio
    )

        category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # Obtiene todas las categorías
        widget=forms.Select(attrs={'class': 'form-control'}),  # Estilo de Bootstrap para el <select>
        required=True  # Asegúrate de que este campo sea obligatorio
        )

        JobOfferTests = forms.ModelMultipleChoiceField(
        queryset=Test.objects.all(),  # Obtener todos los tests disponibles
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Añadir clase CSS para estilo
        required=False,  # Este campo no es obligatorio
    )
    
    
    widgets = {
            'required_hard_skills': forms.CheckboxSelectMultiple(),
            'required_soft_skills': forms.CheckboxSelectMultiple(),
            'JobOfferTests': forms.CheckboxSelectMultiple(),
        }


class ManagementCandidatesForm(forms.ModelForm):
    class Meta:
        model = ManagementCandidates
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['joboffer', 'candidate', 'type_action', 'description', 'date', 'status']
        labels = {
            'candidate': 'Candidato',
            'joboffer': 'Oferta de trabajo',
            'type_action': 'Tipo de acción',
            'description': 'Descripción',
            'date': 'Fecha y hora',
            'status': 'Estado',
        }
        widgets = {
            'joboffer': forms.Select(attrs={'class': 'form-control'}),
            'candidate': forms.Select(attrs={'class': 'form-control'}),
            'type_action': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalles de la acción'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class JobOfferNotificationForm(forms.ModelForm):
    class Meta:
        model = JobOfferNotification
        fields = '__all__'
