from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

    # """URLS"""
urlpatterns = [
    path('', views.home, name='home'),
    path("dashboard/", views.dashboard, name="dashboard"),    
    path("create_test/", views.create_test, name="create_test"),
    path("add_questions/<int:test_id>/", views.add_questions, name="add_questions"),
    path("take_test/<int:test_id>/", views.take_test, name="take_test"),
    path("avalable_tests/", views.available_tests, name="avalable_tests"),    
    path("resolve_json_test/", views.resolve_json_test, name="resolve_json_test"),
    path('test_view', views.quiz_view, name='quiz_view'),  # Initial quiz selection
    path('submit_test/', views.submit_quiz, name='submit_quiz'),  # Handle form submission and result display
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),  # Include the quiz app URLs
    path("submit/", views.submit_quiz, name="submit_quiz"),
]