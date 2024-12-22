from django import forms
from .models import *

# Form to represent a profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_CV
        fields = [
            "user",
            "img_1_profile",
            "img_2_profile",
            "img_3_profile",
            "img_4_profile",
            "address",
            "phone_1",
            "phone_2",
            "email_1",
            "email_2",
            "dni",
            "biography",
            "open_to_work",
            "vehicle",
            "disability",
            "disability_percentage",
        ]

# Form to represent a work experience
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            "job_title",
            "start_date",
            "end_date",
            "current_job",
            "company_name",
            "description",
            "achievements",
            "references",
        ]
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your job title'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'current_job': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your role and responsibilities'
            }),
            'achievements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'List your key achievements and contributions'
            }),
            'references': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add professional references (optional)'
            })
        }

# Form to represent an academic education
class AcademicEducationForm(forms.ModelForm):
    class Meta:
        model = AcademicEducation
        fields = [
            "title",
            "academy_name",
            "start_date",
            "end_date",
            "current_education",
            "references",
        ]
        widgets = {
            'academy_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter academy name'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title or degree name'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'current_education': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'references': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter references or additional information'
            })
        }


# Form to represent a hard skill
class HardSkillForm(forms.ModelForm):
    class Meta:
        model = HardSkillUser
        fields = ["profile_user","hard_skill", "description", "level_skill"]
        widgets ={
            'hard_skill': forms.Select(attrs={
            'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter description'
            }),
            'level_skill': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select a level'
            })
        }

# Form to represent a soft skill
class SoftSkillForm(forms.ModelForm):
    class Meta:
        model = SoftSkillUser
        fields = ["soft_skill", "description"]
        widgets = {
            'soft_skill': forms.Select(attrs={
            'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter description'
            })
        }

# Form to represent a language
class LanguageForm(forms.ModelForm):
    class Meta:
        model = LanguageUser
        fields = ["profile_user","language", "level", "certifications"]
        widgets = {
            'language': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a language'
            }),
            'level': forms.Select(attrs={
                'class': 'form-control',
            }),
            'certifications': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter certifications'
            })
        }

# Form to represent a volunteering
class VolunteeringForm(forms.ModelForm):
    class Meta:
        model = Volunteering
        fields = [
            "volunteering_position",
            "start_date",
            "end_date",
            "current_volunteering",
            "entity_name",
            "description",
            "achievements",
            "references",
        ]
        widgets = {
            'volunteering_position': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the position you are applying for'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'current_volunteering': forms.CheckboxInput(),
            'entity_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the name of the entity'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter a description of the volunteering experience'}),
            'achievements': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter any achievements or awards you have received'}),
            'references': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter any references or sources'}),
        }

# Form to represent a project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "link"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your project and your role in it'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://...'
            })
        }

# Form to represent a publication
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ["doi", "url", "role", "name"]
        widgets = {
            'doi': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter DOI (e.g., 10.1000/xyz123)'
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://...'
            }),
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your role in the publication (e.g., Author, Co-author)'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication title'
            })
        }

# Form to represent a recognition or award
class RecognitionForm(forms.ModelForm):
    class Meta:
        model = RecognitionAward
        fields = ["profile_user","name", "entity", "description"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name of the award or recognition'
            }),
            'entity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name of the awarding organization'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the recognition and its significance'
            })
        }

#form to represent a user cv
class ToggleButtonWidget(forms.CheckboxInput):
    template_name = 'user_cv/button.html'

class ReadOnlyWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'readonly': 'readonly'}
        super().__init__(*args, **kwargs)

class UserCvForm(forms.ModelForm):
    class Meta:
        model = User_cv
        fields = [
            "urlCV",
            "template",
            "has_img_profile",
            "has_address",
            "has_phone_1",
            "has_phone_2",
            "has_email_1",
            "has_email_2",
            "has_dni",
            "has_url",
            "has_biography",
            "has_open_to_work",
            "has_vehicle",
            "has_disability",
            "has_disability_percentage",
            "has_incorporation",
            "has_sector",
            "has_category",
            "has_work_experiences",
            "has_hard_skills",
            "has_soft_skills",
            "has_languages",
            "has_academic_educations",
            "has_volunteerings",
            "has_projects",
            "has_publications",
            "has_recognitions_awards",
            "has_certifications_courses",
            "relations",
        ]
        widgets = {
            'urlCV': ReadOnlyWidget(),
            'has_img_profile': ToggleButtonWidget(),
            'has_address': ToggleButtonWidget(),
            'has_phone_1': ToggleButtonWidget(),
            'has_phone_2': ToggleButtonWidget(),
            'has_email_1': ToggleButtonWidget(),
            'has_email_2': ToggleButtonWidget(),
            'has_dni': ToggleButtonWidget(),
            'has_url': ToggleButtonWidget(),
            'has_biography': ToggleButtonWidget(),
            'has_open_to_work': ToggleButtonWidget(),
            'has_vehicle': ToggleButtonWidget(),
            'has_disability': ToggleButtonWidget(),
            'has_disability_percentage': ToggleButtonWidget(),
            'has_incorporation': ToggleButtonWidget(),
            'has_sector': ToggleButtonWidget(),
            'has_category': ToggleButtonWidget(),
            'has_work_experiences': ToggleButtonWidget(),
            'has_hard_skills': ToggleButtonWidget(),
            'has_soft_skills': ToggleButtonWidget(),
            'has_languages': ToggleButtonWidget(),
            'has_academic_educations': ToggleButtonWidget(),
            'has_volunteerings': ToggleButtonWidget(),
            'has_projects': ToggleButtonWidget(),
            'has_publications': ToggleButtonWidget(),
            'has_recognitions_awards': ToggleButtonWidget(),
            'has_certifications_courses': ToggleButtonWidget(),
        }