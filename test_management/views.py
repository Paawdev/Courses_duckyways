from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Test, UserAnswer, TestResult, Question
from .forms import  TestForm, QuestionForm
from django.conf import settings
from venv import logger
import os
import json
from .forms import QuizSelectForm, QuizForm


def load_quiz(file_name):
    """Load quiz data from the selected JSON file."""
    quiz_path = os.path.join(settings.BASE_DIR, 'quiz', 'static', file_name)
    try:
        with open(quiz_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def quiz_view(request):
    """View to select and load a quiz."""
    if request.method == "POST":
        form = QuizSelectForm(request.POST)
        if form.is_valid():
            quiz_file = form.cleaned_data["quiz_file"]
            quiz_data = load_quiz(quiz_file)

            if quiz_data:
                quiz_form = QuizForm(quiz_data=quiz_data)
                return render(request, "quiz/quiz_form.html", {"quiz_form": quiz_form, "quiz_file": quiz_file})
            else:
                return render(request, "quiz/quiz_select.html", {"form": form, "error": "Quiz file not found."})
    else:
        form = QuizSelectForm()
    return render(request, "quiz/quiz_select.html", {"form": form})


def submit_quiz(request):
    """Handle quiz submission and display results."""
    if request.method == "POST":
        # Retrieve the quiz file name from the hidden input
        quiz_file = request.POST.get("quiz_file")
        quiz_data = load_quiz(quiz_file)

        # Debugging log
        logger.debug(f"Quiz file: {quiz_file}")
        logger.debug(f"POST data: {request.POST}")

        if not quiz_data:
            return render(request, "quiz/quiz_form.html", {"error": "Quiz file not found."})

        # Initialize the QuizForm with the submitted data
        quiz_form = QuizForm(quiz_data, request.POST)
        if quiz_form.is_valid():
            # Calculate the score
            score = 0
            for index, question in enumerate(quiz_data, start=1):
                field_name = f"question_{index}"
                selected_answer = quiz_form.cleaned_data[field_name]
                if selected_answer == question["correct_answer"]:
                    score += 1

            # Render the results page
            return render(request, "quiz/results.html", {"score": score, "total": len(quiz_data)})
        else:
            # Debugging: Show form errors
            logger.debug(f"Form errors: {quiz_form.errors}")

            # Re-render the quiz form with errors
            return render(
                request,
                "quiz/quiz_form.html",
                {"quiz_form": quiz_form, "quiz_file": quiz_file, "error": "Please answer all questions."},
            )

    return render(request, "quiz/quiz_form.html", {"error": "Invalid form submission."})

# TEST CREATION
#listar json, de momento, modificar
@login_required
def create_test(request):
    if not request.user.is_headhunter:
        return redirect("dashboard")

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.created_by = request.user
            test.save()
            return redirect("add_questions", test_id=test.id)
    else:
        form = TestForm()
    return render(request, "test_platform/create_test.html", {"form": form})

                                             
@login_required
def add_questions(request, test_id):
    test = get_object_or_404(Test, id=test_id, created_by=request.user)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.test = test
            question.save()
            return redirect("add_questions", test_id=test.id)
    else:
        form = QuestionForm()
    return render(request, "test_platform/add_questions.html", {"form": form, "test": test})

# TEST TAKING AND SUBMISSION
@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == "POST":
        score = 0
        for question in test.questions.all():
            user_answer = request.POST.get(f"question_{question.id}")
            is_correct = user_answer == question.correct_answer
            UserAnswer.objects.create(
                user=request.user, question=question, selected_answer=user_answer, is_correct=is_correct
            )
            score += 1 if is_correct else 0
        TestResult.objects.create(user=request.user, test=test, score=score)
        return redirect("dashboard")
    return render(request, "test_platform/take_test.html", {"test": test})

# AVAILABLE TESTS
def available_tests(request):
    json_path = settings.BASE_DIR / "static" / "Hard_skills_python.json"
    with open(json_path) as f:
        json_tests = json.load(f)
    db_tests = Test.objects.filter(is_from_json=False)
    return render(request, "test_platform/tests_avalible.html", {"db_tests": db_tests, "json_tests": json_tests})


# RESOLVE JSON TEST
def resolve_json_test(request):
    if request.method == "POST":
        test_data = json.loads(request.POST["test_data"])
        questions = test_data["questions"]
        if "answers" in request.POST:
            answers = request.POST.getlist("answers")
            score = sum(1 for i, q in enumerate(questions) if q["correct_answer"] == answers[i])
            return render(request, "test_platform/test_result.html", {"score": score, "total": len(questions)})
        return render(request, "test_platform/test_resolve.html", {"test": test_data, "questions": questions})
    return redirect("available_tests")

def load_quiz(file_name):
    """Load quiz data from the selected JSON file."""
    quiz_path = os.path.join(settings.BASE_DIR, 'quiz', 'static', file_name)
    try:
        with open(quiz_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
#programar logica de ponderacion vista respuestas.

# View to display quiz selection form
def quiz_view(request):
    if request.method == 'POST':
        # Get the selected quiz file from the form submission
        quiz_file = request.POST.get('quiz_file')

        # Load the selected quiz
        quiz_data = load_quiz(quiz_file)

        if quiz_data:
            return render(request, 'quiz/quiz_form.html', {'quiz_data': quiz_data, 'quiz_file': quiz_file})
        else:
            return render(request, 'quiz/quiz_form.html', {'error': 'Quiz file not found'})

    else:
        # Display the form with the list of quiz files
        quiz_files = [
            'Hard_skills_CSS.json',
            'Hard_skills_Django.json',
            'Hard_skills_HTML.json',
            'Hard_skills_Numpy.json',
            'Hard_skills_SQL.json',
            'Hard_skills_Python.json',
            'Soft_Skills_Test.json'
        ]
        return render(request, 'quiz/quiz_select.html', {'quiz_files': quiz_files})


# View to handle quiz submission and show results

# View to handle quiz submission and show results
def submit_quiz(request):
    if request.method == 'POST':
        quiz_file = request.POST.get('quiz_file')
        quiz_data = load_quiz(quiz_file)

        if not quiz_data:
            return render(request, 'quiz/quiz_form.html', {'error': 'Quiz file not found'})

        score = 0
        for question in quiz_data:
            # Get the selected answer for this question (based on the question index)
            question_id = quiz_data.index(question) + 1  # Unique identifier for the question
            selected_answer = request.POST.get(f'question_{question_id}')  # Get selected answer for this question

            # Log for debugging purposes (optional)
            logger.debug(f"Selected answer for question {question_id}: {selected_answer}")
            logger.debug(f"Correct answer for question {question_id}: {question['correct_answer']}")

            # Compare the selected answer with the correct one
            if selected_answer == question['correct_answer']:
                score += 1

        # Return results to the user
        return render(request, 'quiz/results.html', {'score': score, 'total': len(quiz_data)})

    return render(request, 'quiz/quiz_form.html', {'error': 'Invalid form submission'})


