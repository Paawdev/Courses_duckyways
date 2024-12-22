from django import forms
from django.contrib.auth.models import *
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ResourceCourseForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'image', 'url', 'document']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'image', 'url', 'document', 'price']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'code', 'ext_certificate']
        
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description', 'is_active']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'description', 'duration']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'max': 5, 'min': 1}),  # Asegúrate de que el rating sea un número entre 1 y 5
            'comment': forms.Textarea(attrs={'placeholder': 'Leave your comment here...'}),
        }

class CourseSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

class ResourceSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)


class ProfileTeacherForm(forms.ModelForm):
    class Meta:
        model = ProfileTeacher
        fields = ['bio', 'image', 'hardskills', 'category', 'sector']

