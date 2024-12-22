from django import forms
import re
from .models import User, Test, Question
from django.contrib.auth.forms import AuthenticationForm
#registro usuario lo hace oscar
# Formulario de registro de usuario 


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'description', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'duration': forms.NumberInput(attrs={"class": "form-control"}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content', 'question_type', 'options', 'correct_answer']
        widgets = {
            'content': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el contenido de la pregunta"}),
            'question_type': forms.Select(attrs={"class": "form-control"}),
            'options': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese las opciones separadas por comas"}),
            'correct_answer': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese la respuesta correcta"}),
        }

    def clean_content(self):
        """Validación del campo 'content': debe contener solo caracteres alfanuméricos y espacios."""
        content = self.cleaned_data.get('content')
        content_regex = r'^[a-zA-Z0-9\s]+$'
        if not re.match(content_regex, content):
            raise forms.ValidationError("El contenido solo puede contener letras, números y espacios.")
        return content

    def clean_options(self):
        """
        Validación del campo 'options': debe ser una lista separada por comas.
        Cada opción debe contener caracteres alfanuméricos.
        """
        options = self.cleaned_data.get('options')
        options_regex = r'^[a-zA-Z0-9\s,]+$'
        if not re.match(options_regex, options):
            raise forms.ValidationError("Las opciones deben estar separadas por comas y contener solo letras, números y espacios.")
        # Verificar que haya al menos dos opciones
        options_list = [opt.strip() for opt in options.split(',')]
        if len(options_list) < 2:
            raise forms.ValidationError("Debe ingresar al menos dos opciones separadas por comas.")
        return options

    def clean_correct_answer(self):
        """
        Validación del campo 'correct_answer': debe coincidir con una de las opciones ingresadas.
        """
        correct_answer = self.cleaned_data.get('correct_answer')
        options = self.cleaned_data.get('options')
        if options:
            options_list = [opt.strip() for opt in options.split(',')]
            if correct_answer not in options_list:
                raise forms.ValidationError("La respuesta correcta debe coincidir con una de las opciones.")
        return correct_answer

# Formulario de creación de pruebas
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        title_regex = r'^[a-zA-Z0-9\s]+$'
        if not re.match(title_regex, title):
            raise forms.ValidationError("El título solo puede contener letras, números y espacios.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        description_regex = r'^[a-zA-Z0-9\s,.!?]*$'
        if description and not re.match(description_regex, description):
            raise forms.ValidationError(
                "La descripción solo puede contener letras, números, espacios, comas, puntos, signos de exclamación e interrogación."
            )
        return description
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    user_type = forms.ChoiceField(
        choices=[('regular', 'Regular User'), ('headhunter', 'Headhunter')],
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'user_type']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
    }

class QuizSelectForm(forms.Form):
    """Form for selecting a quiz file."""
    quiz_file = forms.ChoiceField(
        choices=[
            ('Hard_skills_CSS.json', 'CSS'),
            ('Hard_skills_Django.json', 'Django'),
            ('Hard_skills_HTML.json', 'HTML'),
            ('Hard_skills_Numpy.json', 'Numpy'),
            ('Hard_skills_SQL.json', 'SQL'),
            ('Hard_skills_Python.json', 'Python'),
            ('Soft_Skills_Test.json', 'Soft Skills'),
        ],
        label="Select a quiz",
    )

class QuizForm(forms.Form):
    """Dynamic form for taking a quiz."""

    def __init__(self, quiz_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for index, question in enumerate(quiz_data, start=1):
            field_name = f"question_{index}"
            self.fields[field_name] = forms.ChoiceField(
                choices=[(answer, answer) for answer in question["answers"]],
                widget=forms.RadioSelect,
                label=question["question"],
                required=True,
            )
