import random
import string
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from weasyprint import HTML
from .models import *
from .forms import *
from django.template.loader import get_template
from django.contrib.auth.models import User
from courses.models import Course

# * |--------------------------------------------------------------------------
# * | Home
# * |--------------------------------------------------------------------------

#? Función para la página de inicio
def home(request):
    return render(request, "base.html")

# * |--------------------------------------------------------------------------
# * | Class Profile
# * |--------------------------------------------------------------------------

# ? Función para crear un perfil
def profile_create(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm()
    return render(request, "profile/profile_form.html", {"form": form})

# ? Función para listar los perfiles
def profile_list(request):
    profiles = Profile_CV.objects.all()
    return render(request, "profile/profile_list.html", {"profiles": profiles})

# ? Función para actualizar un perfil
def profile_update(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    if request.method == "POST":
        form = ProfileForm(request.POST,  request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile/profile_form.html", {"form": form})

# ? Función para eliminar un perfil
def profile_delete(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    if request.method == "POST":
        profile.delete()
        return redirect("profile_list")
    return render(request, "profile/profile_confirm_delete.html", {"profile": profile})

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    return render(request, 'profile/profile_view_details.html', {'profile': profile})

# * |--------------------------------------------------------------------------
# * | Class WorkExperience
# * |--------------------------------------------------------------------------

# ? Función para crear una experiencia laboral
def work_experience_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.profile_user = profile
            form.save()
            return redirect("work_experience_list")
    else:
        form = WorkExperienceForm()
    return render(request, "work_experience/work_experience_form.html", {"form": form, "user": user})

# ? Función para listar las experiencias laborales
def work_experience_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    work_experiences = WorkExperience.objects.filter(profile_user=profile)
    return render(request, "work_experience/work_experience_list.html", {"work_experiences": work_experiences, "user": user})

# ? Función para actualizar una experiencia laboral
def work_experience_update(request, work_experience_id):
    work_experience = get_object_or_404(WorkExperience, id=work_experience_id)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect("work_experience_list")
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, "work_experience/work_experience_form.html", {"form": form})

# ? Función para eliminar una experiencia laboral
def work_experience_delete(request, work_experience_id):
    work_experience = get_object_or_404(WorkExperience, id=work_experience_id)
    if request.method == "POST":
        work_experience.delete()
        return redirect("work_experience_list")
    return render(request, "work_experience/work_experience_confirm_delete.html", {"work_experience": work_experience})

# * |--------------------------------------------------------------------------
# * | Class AcademicEducation
# * |--------------------------------------------------------------------------

# ? Función para crear una educación académica
def academic_education_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = AcademicEducationForm(request.POST)
        if form.is_valid():
            academic_education = form.save(commit=False)
            academic_education.profile_user = profile
            form.save()
            return redirect("academic_education_list")
    else:
        form = AcademicEducationForm()
    return render(request, "academic_education/academic_education_form.html", {"form": form, "user": user})

# ? Función para listar las educaciones académicas
def academic_education_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    academic_educations = AcademicEducation.objects.filter(profile_user=profile)
    return render(request, "academic_education/academic_education_list.html", {"academic_educations": academic_educations, "user": user})

# ? Función para actualizar una educación académica
def academic_education_update(request, academic_education_id):
    academic_education = get_object_or_404(AcademicEducation, id=academic_education_id)
    if request.method == "POST":
        form = AcademicEducationForm(request.POST, instance=academic_education)
        if form.is_valid():
            form.save()
            return redirect("academic_education_list")
    else:
        form = AcademicEducationForm(instance=academic_education)
    return render(request, "academic_education/academic_education_form.html", {"form": form})

# ? Función para eliminar una educación académica
def academic_education_delete(request, academic_education_id):
    academic_education = get_object_or_404(AcademicEducation, id=academic_education_id)
    if request.method == "POST":
        academic_education.delete()
        return redirect("academic_education_list")
    return render(request, "academic_education/academic_education_confirm_delete.html", {"academic_education": academic_education})

# * |--------------------------------------------------------------------------
# * | Class SoftSkill
# * |--------------------------------------------------------------------------

#? Función para listar las SoftSkills
def softskill_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    softskills = SoftSkillUser.objects.filter(profile_user=profile)
    return render(request, "softskill/softskill_list.html", {"softskills": softskills, "user": user})

#? Función para crear una SoftSkill
def softskill_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = SoftSkillForm(request.POST)
        if form.is_valid():
            soft_skill = form.save(commit=False)
            soft_skill.profile_user = profile
            form.save()
            return redirect("soft_skill_list")
    else:
        form = SoftSkillForm()
    return render(request, "softskill/softskill_form.html", {"form": form, "user": user})

#? Función para actualizar una SoftSkill
def softskill_update(request, soft_skill_id):
    softskill = get_object_or_404(SoftSkillUser, id=soft_skill_id)
    if request.method == "POST":
        form = SoftSkillForm(request.POST, instance=softskill)
        if form.is_valid():
            form.save()
            return redirect("soft_skill_list")
    else:
        form = SoftSkillForm(instance=softskill)
    return render(request, "softskill/softskill_form.html", {"form": form})

#? Función para eliminar una SoftSkill
def softskill_delete(request, soft_skill_id):
    softskill = get_object_or_404(SoftSkillUser, id=soft_skill_id)
    if request.method == "POST":
        softskill.delete()
        return redirect("soft_skill_list")
    return render(request, "softskill/softskill_confirm_delete.html", {"softskill": softskill})

# * |--------------------------------------------------------------------------
# * | Class HardSkill
# * |--------------------------------------------------------------------------

#? Función para listar las HardSkills
def hardskill_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile= get_object_or_404(Profile_CV,  user=user)
    hardskills = HardSkillUser.objects.filter(profile_user = profile)
    return render(request, "hardskill/hardskill_list.html", {"hardskills": hardskills, 'user': user})


#? Función para crear una HardSkill
def hardskill_create(request, user_id):
    user = get_object_or_404(User, id= user_id)
    profile = get_object_or_404(Profile_CV, user = user)
    if request.method == "POST":
        form = HardSkillForm(request.POST)
        if form.is_valid():
            hardskill = form.save(commit  = False)
            hardskill.profile_user = profile
            form.save()
            return redirect("hard_skill_list")
    else:
        form = HardSkillForm()
    return render(request, "hardskill/hardskill_form.html", {"form": form, 'user': user})

# ? Función para actualizar una educación académica
def academic_education_update(request, academic_education_id):
    academic_education = get_object_or_404(AcademicEducation, id=academic_education_id)
    if request.method == "POST":
        form = AcademicEducationForm(request.POST, instance=academic_education)
        if form.is_valid():
            form.save()
            return redirect("academic_education_list")
    else:
        form = AcademicEducationForm(instance=academic_education)
    return render(request, "academic_education/academic_education_form.html", {"form": form})

#? Función para eliminar una HardSkill
def hardskill_delete(request, hard_skill_id):
    hardskill = get_object_or_404(HardSkillUser, id=hard_skill_id)
    if request.method == "POST":
        hardskill.delete()
        return redirect("hard_skill_list")
    return render(request, "hardskill/hardskill_confirm_delete.html", {"hardskill": hardskill})

# * |--------------------------------------------------------------------------
# * | language
# * |--------------------------------------------------------------------------

#? Función para listar los idiomas
def language_list(request, user_id):
    user = get_object_or_404(User, id = user_id)
    profile = get_object_or_404(Profile_CV, user = user)
    languages = LanguageUser.objects.filter(profile_user = profile)
    return render(request, "language/language_list.html", {"languages": languages, 'user': user})

#? Función para crear un idioma
def language_create(request, user_id):
    user = get_object_or_404(User, id= user_id)
    profile = get_object_or_404(Profile_CV, user= user)
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit = False)
            language.profile_user = profile
            form.save()
            return redirect("language_list")
    else:
        form = LanguageForm()
    return render(request, "language/language_form.html", {"form": form, 'user':user})

#? Función para actualizar un idioma
def language_update(request, language_id):
    language = get_object_or_404(LanguageUser, id=language_id)
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect("language_list")
    else:
        form = LanguageForm(instance=language)
    return render(request, "language/language_form.html", {"form": form})

#? Función para eliminar un idioma
def language_delete(request, language_id):
    language = get_object_or_404(LanguageUser, id=language_id)
    if request.method == "POST":
        language.delete()
        return redirect("language_list")
    return render(request, "language/language_confirm_delete.html", {"language": language})

# * |--------------------------------------------------------------------------
# * | Class Volunteering
# * |--------------------------------------------------------------------------

#? Función para listar los voluntariados
def volunteering_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    volunteerings = Volunteering.objects.filter(profile_user=profile)
    return render(request, "volunteering/volunteering_list.html", {"volunteerings": volunteerings, "user": user})

#? Función para crear un voluntariado
def volunteering_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = VolunteeringForm(request.POST)
        if form.is_valid():
            volunteering = form.save(commit=False)
            volunteering.profile_user = profile
            form.save()
            return redirect("volunteering_list")
    else:
        form = VolunteeringForm()
    return render(request, "volunteering/volunteering_form.html", {"form": form, "user": user})

#? Función para actualizar un voluntariado
def volunteering_update(request, volunteering_id):
    volunteering = get_object_or_404(Volunteering, id=volunteering_id)
    if request.method == "POST":
        form = VolunteeringForm(request.POST, instance=volunteering)
        if form.is_valid():
            form.save()
            return redirect("volunteering_list")
    else:
        form = VolunteeringForm(instance=volunteering)
    return render(request, "volunteering/volunteering_form.html", {"form": form})

#? Función para eliminar un voluntariado
def volunteering_delete(request, volunteering_id):
    volunteering = get_object_or_404(Volunteering, id=volunteering_id)
    if request.method == "POST":
        volunteering.delete()
        return redirect("volunteering_list")
    return render(request, "volunteering/volunteering_confirm_delete.html", {"volunteering": volunteering})

# * |--------------------------------------------------------------------------
# * | Class Project
# * |--------------------------------------------------------------------------

#? Función para listar los proyectos
def project_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    projects = Project.objects.filter(profile_user=profile)
    return render(request, "project/project_list.html", {"projects": projects, "user": user})

#? Función para crear un proyecto
def project_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile_user = profile
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "project/project_form.html", {"form": form, "user": user})

#? Función para actualizar un proyecto
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "project/project_form.html", {"form": form})

#? Función para eliminar un proyecto
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    return render(request, "project/project_confirm_delete.html", {"project": project})

# * |--------------------------------------------------------------------------
# * | Class RecognitionAward
# * |--------------------------------------------------------------------------

#? Función para listar los reconocimientos y premios
def recognition_award_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    recognitions_awards = RecognitionAward.objects.filter(profile_user=profile)
    return render(request, "recognitionaward/recognitionaward_list.html", {"recognitions_awards": recognitions_awards, "user": user})

#? Función para crear un reconocimiento o premio
def recognition_award_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = RecognitionForm(request.POST)
        if form.is_valid():
            recognitionaward = form.save(commit=False)
            recognitionaward.profile_user = profile
            form.save()
            return redirect("recognition_award_list")
    else:
        form = RecognitionForm()
    return render(request, "recognitionaward/recognitionaward_form.html", {"form": form, "user": user})

#? Función para actualizar un reconocimiento o premio
def recognition_award_update(request, recognition_award_id):
    recognitionaward = get_object_or_404(RecognitionAward, id=recognition_award_id)
    if request.method == "POST":
        form = RecognitionForm(request.POST, instance=recognitionaward)
        if form.is_valid():
            form.save()
            return redirect("recognition_award_list")
    else:
        form = RecognitionForm(instance=recognitionaward)
    return render(request, "recognitionaward/recognitionaward_form.html", {"form": form})

#? Función para eliminar un reconocimiento o premio
def recognition_award_delete(request, recognition_award_id):
    recognitionaward = get_object_or_404(RecognitionAward, id=recognition_award_id)
    if request.method == "POST":
        recognitionaward.delete()
        return redirect("recognition_award_list")
    return render(request, "recognitionaward/recognitionaward_confirm_delete.html", {"recognitions_awards": recognitionaward})

# * |--------------------------------------------------------------------------
# * | Class Publication
# * |--------------------------------------------------------------------------

#? Función para listar las publicaciones
def publication_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    publications = Publication.objects.filter(profile_user=profile)
    return render(request, "publication/publication_list.html", {"publications": publications, "user": user})

#? Función para crear una publicación
def publication_create(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile_CV, user=user)
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.profile_user = profile
            form.save()
            return redirect("publication_list")
    else:
        form = PublicationForm()
    return render(request, "publication/publication_form.html", {"form": form, "user": user})

#? Función para actualizar una publicación
def publication_update(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect("publication_list")
    else:
        form = PublicationForm(instance=publication)
    return render(request, "publication/publication_form.html", {"form": form})

#? Función para eliminar una publicación
def publication_delete(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == "POST":
        publication.delete()
        return redirect("publication_list")
    return render(request, "publication/publication_confirm_delete.html", {"publication": publication})

# * |--------------------------------------------------------------------------
# * | User_CV
# * |--------------------------------------------------------------------------

#? Función para listar los CV
def user_cv_list(request, profile_id):
    profile = get_object_or_404(Profile_CV, id=profile_id)
    user_cv = User_cv.objects.filter(profile_user=profile)
    return render(request, "user_cv/user_cv_list.html", {"user_cv": user_cv})

#? Función para crear un CV
def user_cv_create(request, profile_id):
    profile_cv = get_object_or_404(Profile_CV, id=profile_id)
    user_cv = User_cv.objects.filter(profile_user=profile_cv)
    work_experiences = WorkExperience.objects.filter(profile_user=profile_cv)
    academic_educations = AcademicEducation.objects.filter(profile_user=profile_cv)
    hard_skills = HardSkillUser.objects.filter(profile_user=profile_cv)
    soft_skills = SoftSkillUser.objects.filter(profile_user=profile_cv)
    languages = LanguageUser.objects.filter(profile_user=profile_cv)
    categories = CategoryUser.objects.filter(profile_user=profile_cv)
    sectors = SectorUser.objects.filter(profile_user=profile_cv)
    incorporations = IncorporationUser.objects.filter(profile_user=profile_cv)
    volunteerings = Volunteering.objects.filter(profile_user=profile_cv)
    projects = Project.objects.filter(profile_user=profile_cv)
    publications = Publication.objects.filter(profile_user=profile_cv)
    recognitions_awards = RecognitionAward.objects.filter(profile_user=profile_cv)

    if request.method == "POST":
        form = UserCvForm(request.POST)
        if form.is_valid():
            user_cv = form.save(commit=False)
            user_cv.profile_user = profile_cv  # Asigna el perfil del usuario
            user_cv.save()

            # Obtener las experiencias laborales seleccionadas
            selected_experiences = request.POST.getlist('work_experiences')
            for experience_id in selected_experiences:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    work_experience_id=experience_id
                )

            # Obtener las educaciones académicas seleccionadas
            selected_academic_educations = request.POST.getlist('academic_educations')
            for education_id in selected_academic_educations:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    academic_education_id=education_id
                )

            # Obtener las habilidades duras seleccionadas
            selected_hard_skills = request.POST.getlist('hard_skills')
            for skill_id in selected_hard_skills:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    hard_skill_id=skill_id
                )

            # Obtener las habilidades blandas seleccionadas
            selected_soft_skills = request.POST.getlist('soft_skills')
            for skill_id in selected_soft_skills:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    soft_skill_id=skill_id
                )

            # Obtener los idiomas seleccionados
            selected_languages = request.POST.getlist('languages')
            for language_id in selected_languages:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    language_id=language_id
                )

            # Obtener las categorías seleccionadas
            selected_categories = request.POST.getlist('categories')
            for category_id in selected_categories:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    category_id=category_id
                )

            # Obtener los sectores seleccionados
            selected_sectors = request.POST.getlist('sectors')
            for sector_id in selected_sectors:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    sector_id=sector_id
                )

            # Obtener las incorporaciones seleccionadas
            selected_incorporations = request.POST.getlist('incorporations')
            for incorporation_id in selected_incorporations:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    incorporation_id=incorporation_id
                )

            # Obtener los voluntariados seleccionados
            selected_volunteerings = request.POST.getlist('volunteerings')
            for volunteering_id in selected_volunteerings:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    volunteering_id=volunteering_id
                )

            # Obtener los proyectos seleccionados
            selected_projects = request.POST.getlist('projects')
            for project_id in selected_projects:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    project_id=project_id
                )

            # Obtener las publicaciones seleccionadas
            selected_publications = request.POST.getlist('publications')
            for publication_id in selected_publications:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    publication_id=publication_id
                )

            # Obtener los reconocimientos y premios seleccionados
            selected_recognitions = request.POST.getlist('recognitions_awards')
            for recognition_id in selected_recognitions:
                UserCvRelation.objects.create(
                    user_cv=user_cv,
                    recognition_award_id=recognition_id
                )
            
            # Obtener cursos
            # selected_course = request.POST.getlist('course')
            # for course_id in selected_course:
            #     UserCvRelation.objects.create(
            #         user_cv=user_cv,
            #         course_id=course_id
            #     )

            return redirect("user_cv_list", profile_id)  # Pasa el profile_id aquí
    else:
        random_numbers = ''.join(random.choices(string.digits, k=4))
        initial_urlCV = f"https://{profile_cv.user.username}-{random_numbers}.com"
        form = UserCvForm(initial={'urlCV': initial_urlCV})

    context = {
        'form': form,
        'profile_cv': profile_cv,
        'work_experiences': work_experiences,
        'academic_educations': academic_educations,
        'hard_skills': hard_skills,
        'soft_skills': soft_skills,
        'languages': languages,
        'categories': categories,
        'sectors': sectors,
        'incorporations': incorporations,
        'volunteerings': volunteerings,
        'projects': projects,
        'publications': publications,
        "courses": profile_cv.user.enrolled_courses.filter(status__name='completed'),
        'recognitions_awards': recognitions_awards,
    }

    return render(request, "user_cv/user_cv_form.html", context)

#? Función para actualizar un CV
def user_cv_update(request, user_cv_id):
    user_cv = get_object_or_404(User_cv, id=user_cv_id)
    profile_id = user_cv.profile_user.id  # Obtén el profile_id del user_cv
    profile_cv = get_object_or_404(Profile_CV, id=profile_id)
    if request.method == "POST":
        form = UserCvForm(request.POST, instance=user_cv)
        if form.is_valid():
            form.save()
            return redirect("user_cv_list", profile_id=profile_id)  # Pasa el profile_id aquí
    else:
        form = UserCvForm(instance=user_cv)
    return render(request, "user_cv/user_cv_form.html", {"form": form, "user_cv": user_cv, "profile_cv": profile_cv})

#? Función para eliminar un CV
def user_cv_delete(request, user_cv_id):
    user_cv = get_object_or_404(User_cv, id=user_cv_id)
    profile_id = user_cv.profile_user.id  # Obtén el profile_id del user_cv

    if request.method == "POST":
        user_cv.delete()
        return redirect("user_cv_list", profile_id=profile_id)  # Pasa el profile_id aquí
    return render(request, "user_cv/user_cv_confirm_delete.html", {"user_cv": user_cv})

#? Función para ver los detalles de un CV
def user_cv_view_details(request, user_cv_id, profile_cv_id):
    user_cv = get_object_or_404(User_cv, id=user_cv_id)
    profile_cv = get_object_or_404(Profile_CV, id=profile_cv_id)

    # Filtrar solo los campos asociadas al User_cv
    user_cv_relations = UserCvRelation.objects.filter(user_cv=user_cv)

    work_experiences = WorkExperience.objects.filter(id__in=user_cv_relations.values('work_experience'))
    academic_educations = AcademicEducation.objects.filter(id__in=user_cv_relations.values('academic_education'))
    hard_skills = HardSkillUser.objects.filter(id__in=user_cv_relations.values('hard_skill'))
    soft_skills = SoftSkillUser.objects.filter(id__in=user_cv_relations.values('soft_skill'))
    languages = LanguageUser.objects.filter(id__in=user_cv_relations.values('language'))
    categories = CategoryUser.objects.filter(id__in=user_cv_relations.values('category'))
    sectors = SectorUser.objects.filter(id__in=user_cv_relations.values('sector'))
    incorporations = IncorporationUser.objects.filter(id__in=user_cv_relations.values('incorporation'))
    volunteerings = Volunteering.objects.filter(id__in=user_cv_relations.values('volunteering'))
    projects = Project.objects.filter(id__in=user_cv_relations.values('project'))
    publications = Publication.objects.filter(id__in=user_cv_relations.values('publication'))
    recognitions_awards = RecognitionAward.objects.filter(id__in=user_cv_relations.values('recognition_award'))

    context = {
        'user_cv': user_cv,
        'profile_cv': profile_cv,
        'work_experiences': work_experiences,
        'academic_educations': academic_educations,
        'hard_skills': hard_skills,
        'soft_skills': soft_skills,
        'languages': languages,
        'categories': categories,
        'sectors': sectors,
        'incorporations': incorporations,
        'volunteerings': volunteerings,
        'projects': projects,
        'publications': publications,
        'recognitions_awards': recognitions_awards,
    }

    return render(request, 'user_cv/user_cv_view_details.html', context)

def user_cv_pdf_view(request, user_cv_id, profile_cv_id):
    # user_cv = get_object_or_404(User_cv, id=user_cv_id)
    # profile_cv = get_object_or_404(Profile_CV, id=profile_cv_id)
    # work_experiences = WorkExperience.objects.filter(profile_user=profile_cv)
    # academic_educations = AcademicEducation.objects.filter(profile_user=profile_cv)
    # hard_skills = HardSkillUser.objects.filter(profile_user=profile_cv)
    # soft_skills = SoftSkillUser.objects.filter(profile_user=profile_cv)
    # languages = LanguageUser.objects.filter(profile_user=profile_cv)
    # categories = CategoryUser.objects.filter(profile_user=profile_cv)
    # sectors = SectorUser.objects.filter(profile_user=profile_cv)
    # incorporations = IncorporationUser.objects.filter(profile_user=profile_cv)
    # volunteerings = Volunteering.objects.filter(profile_user=profile_cv)
    # projects = Project.objects.filter(profile_user=profile_cv)
    # publications = Publication.objects.filter(profile_user=profile_cv)
    # recognitions_awards = RecognitionAward.objects.filter(profile_user=profile_cv)

    # context = {
    #     'user_cv': user_cv,
    #     'profile_cv': profile_cv,
    #     'work_experiences': work_experiences,
    #     'academic_educations': academic_educations,
    #     'hard_skills': hard_skills,
    #     'soft_skills': soft_skills,
    #     'languages': languages,
    #     'categories': categories,
    #     'sectors': sectors,
    #     'incorporations': incorporations,
    #     'volunteerings': volunteerings,
    #     'projects': projects,
    #     'publications': publications,
    #     'recognitions_awards': recognitions_awards,
    # }

    # template = get_template('user_cv/user_cv_view_details.html')
    # html_content = template.render(context)

    # pdf_file = HTML(string=html_content).write_pdf()

    # response = HttpResponse(pdf_file, content_type='application/pdf')
    # response['Content-Disposition'] = "inline; filename='user_cv.pdf'"

    return response