from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Obtén los grupos del usuario
    user_groups = request.user.groups.all()
    
    # Verifica el grupo del usuario
    user_role = None
    if user_groups.exists():
        user_role = user_groups[0].name  # Obtén el nombre del primer grupo asociado al usuario
    context = {}  # Inicializa el contexto

    if user_role == 'premium' or user_role == 'freemium':
        # context = {
        #     'user_role': user_role,
        #     'profile_user': getattr(request.user, 'profile_user', None),
        # }
        # return render(request, 'role_management/dashboard_premium.html', context)
        return redirect('premium_dashboard')

    elif user_role == 'teacher':
        # context = {
        #     'user_role': user_role,
        #     'profile_teacher': getattr(request.user, 'profile_teacher', None),
        # }
        # return render(request, 'role_management/dashboard_teacher.html', context)
        return redirect('teacher_dashboard')

    elif user_role == 'headhunter':
        context = {
            'user_role': user_role,
            'profile_headhunter': getattr(request.user, 'profile_headhunter', None),
        }
        return render(request, 'role_management/dashboard_headhunter.html', context)

    else:
        # Maneja el caso en que no tenga un grupo o no sea reconocido
        context = {
            'user_role': 'unknown',
            'message': 'Role not recognized or user not logged in.',
        }
        return render(request, 'role_management/dashboard_default.html', context)

@login_required
def teacher_chat(request):
    # Verifica que el usuario tenga el rol de "teacher"
    user_groups = request.user.groups.all()
    if not user_groups.filter(name="teacher").exists():
        # Si el usuario no es un "teacher", redirige o muestra un mensaje de error
        return render(request, 'role_management/access_denied.html', {
            'message': 'You do not have permission to access this page.',
        })
    
    # Define el contexto para la vista
    context = {
        'user_role': 'teacher',
        'teacher_profile': getattr(request.user, 'profile_teacher', None),
        # Agrega aquí más datos relacionados con el rol de "teacher"
    }
    return render(request, 'role_management/teacher_chat.html', context)

@login_required
def headhunter_chat(request):
    # Verifica que el usuario tenga el rol de "teacher"
    user_groups = request.user.groups.all()
    if not user_groups.filter(name="headhunter").exists():
        # Si el usuario no es un "teacher", redirige o muestra un mensaje de error
        return render(request, 'role_management/access_denied.html', {
            'message': 'You do not have permission to access this page.',
        })
    
    # Define el contexto para la vista
    context = {
        'user_role': 'headhunter',
        'teacher_profile': getattr(request.user, 'headhunter', None),
        # Agrega aquí más datos relacionados con el rol de "teacher"
    }
    return render(request, 'role_management/headhunter_chat.html', context)

@login_required
def premium_chat(request):
    # Verifica que el usuario tenga el rol de "teacher"
    user_groups = request.user.groups.all()
    if not user_groups.filter(name="premium").exists():
        # Si el usuario no es un "premium", redirige o muestra un mensaje de error
        return render(request, 'role_management/access_denied.html', {
            'message': 'You do not have permission to access this page.',
        })
    
    # Define el contexto para la vista
    context = {
        'user_role': 'premium',
        'teacher_profile': getattr(request.user, 'profile_user', None),
        # Agrega aquí más datos relacionados con el rol de "teacher"
    }
    return render(request, 'role_management/premium_chat.html', context)

@login_required
def teacher_dashboard(request):
    return redirect('courses:teacher-course-list')

@login_required
def headhunter_dashboard(request):
    # Verifica que el usuario tenga el rol de "teacher"
    user_groups = request.user.groups.all()
    if not user_groups.filter(name="headhunter").exists():
        # Si el usuario no es un "teacher", redirige o muestra un mensaje de error
        return render(request, 'role_management/access_denied.html', {
            'message': 'You do not have permission to access this page.',
        })
    
    # Define el contexto para la vista
    context = {
        'user_role': 'headhunter',
        'headhunter_profile': getattr(request.user, 'headhunter', None),
        # Agrega aquí más datos relacionados con el rol de "teacher"
    }
    return render(request, 'role_management/dashboard_headhunter.html', context)


@login_required
def premium_dashboard(request):
    # Verifica que el usuario tenga el rol de "teacher"
    user_freemium = request.user.groups.filter(name="freemium").exists()
    user_premium = request.user.groups.filter(name="premium").exists()
    if not user_freemium and not user_premium:
        # Si el usuario no es un "premium", redirige o muestra un mensaje de error
        return render(request, 'role_management/access_denied.html', {
            'message': 'You do not have permission to access this page.',
        })
    # Define el contexto para la vista
    context = {
        'user_role': 'freemium' if user_freemium else 'premium',
    }
    return render(request, 'role_management/dashboard_premium.html', context)

@login_required
def premium_profile(request):
    # Verifica que el usuario tenga el rol de "profile"
    user_groups = request.user.groups.all()
    if not user_groups.filter(name="premium").exists():
        # Si el usuario no es un "premium", redirige o muestra un mensaje de error
        return render(request, 'role_management/access_denied.html', {
            'message': 'You do not have permission to access this page.',
        })
    
    # Define el contexto para la vista
    context = {
        'user_role': 'premium',
        'teacher_profile': getattr(request.user, 'profile_user', None),
        # Agrega aquí más datos relacionados con el rol de "teacher"
    }
    return render(request, 'role_management/premium_profile.html', context)