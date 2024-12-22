from django.db import models
from django.contrib.auth.models import User


# Create Models Here

class Test(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tests")
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    is_from_json = models.BooleanField(default=False)
    #soft skills relacion con tabla grupo montse
    #hard skills relacion con tabla grupo montse

class QuestionType(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=200)
class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)    
    selected_answer =  models.ForeignKey(Answer, on_delete=models.CASCADE) 
    is_correct = models.BooleanField()
    #relacionar hard skills con user test

class UserTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

class CatergoryType(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Catergory(models.Model):
    name = models.CharField(max_length=200) 
    type = models.ForeignKey(CatergoryType, on_delete=models.CASCADE)


