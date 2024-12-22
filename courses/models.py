from decimal import Decimal
from django.db import models
from django.forms import ValidationError
from profile_cv.models import HardSkill, Sector, Category

from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ProfileTeacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_teacher") # para usar la query --> user.profile_teacher.get(id=1)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='teachers_images/', null=True, blank=True)
    hardskills = models.ForeignKey(HardSkill, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'


class Course(models.Model):
    profile_teacher = models.ForeignKey(ProfileTeacher, on_delete=models.CASCADE, related_name="courses") # para usar la query --> profile_teacher.courses.all()
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    is_member = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='courses_images/', default='courses_images/default.jpg', null=True, blank=True)
    is_free = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    hardskills = models.ManyToManyField(HardSkill, blank=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="certificates") # para usar la query --> user.enrolled_courses.all()
    is_course_cert = models.BooleanField(default=True)
    ext_certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    user = models.ManyToManyField(User, blank=True, related_name="certificates") # para usar la query --> user.certificates.all()

    def clean(self):
        # Si es un certificado externo (course_cert=False), asegurarse que solo tenga un usuario asignado
        if not self.course_cert and self.user.count() > 1:
            raise ValidationError("An external certificate can only belong to one user.")

    def save(self, *args, **kwargs):
        self.clean()  # Validar antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.code}'

class Review(models.Model):
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name="reviews") # para usar la query --> course.reviews.all()
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, null=True, blank=True, related_name="reviews") # para usar la query --> resource.reviews.all()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            # Garantiza que una Review solo pueda estar vinculada a un curso o a un recurso
            models.CheckConstraint(
                check=(
                    models.Q(course__isnull=False, resource__isnull=True) |
                    models.Q(course__isnull=True, resource__isnull=False)
                ),
                name='review_course_or_resource_not_both'
            ),
            # Asegura que un usuario pueda dejar solo una review por curso
            models.UniqueConstraint(
                fields=['user', 'course'],
                name='unique_user_course_review'
            ),
            # Asegura que un usuario pueda dejar solo una review por recurso
            models.UniqueConstraint(
                fields=['user', 'resource'],
                name='unique_user_resource_review'
            )
        ]

    def __str__(self):
        if self.course:
            return f'{self.user.username} - Course: {self.course.title}'
        elif self.resource:
            return f'{self.user.username} - Resource: {self.resource.name}'
        else:
            return f'{self.user.username} - Unlinked Review'


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules") # para usar la query --> course.modules.all()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons") # para usar la query --> module.lessons.all()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_member = models.BooleanField(default=False)
    duration = models.IntegerField(null=True, blank=True, default=10)

    def __str__(self):
        return f'{self.module} - {self.name}'

class CourseUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrolled_courses") # para usar la query --> user.enrolled_courses.all()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrolled_users") # para usar la query --> course.enrolled_users.all()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    certified = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], name='unique_user_course')
        ]

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.course}'


class Resource(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null=True, related_name='resources') # para usar la query --> lesson.resources.all()
    name = models.CharField(max_length=255, unique=True)
    downloadable = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True, upload_to='resources_images/')
    url = models.URLField(blank=True, null=True)
    document = models.FileField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    hardskill = models.ManyToManyField(HardSkill, blank=True, related_name='hardskills')

    def __str__(self):
        return f"{self.name}"

class WishListType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class WishListUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")# para usar la query --> user.wishlist.all()
    type_wish = models.ForeignKey(WishListType, on_delete=models.CASCADE)
    id_wish = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.type_wish.name}"


class LessonCompletion(models.Model):
    course_user = models.ForeignKey(CourseUser, on_delete=models.CASCADE, related_name="lessons_completed") # para usar la query --> course_user.user_lessons_completed.all()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="users_completed_lessons") # para usar la query --> lesson.users_completed_lessons.all()
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('course_user', 'lesson')

    def __str__(self):
        return f"{self.course_user.user.username} - {self.lesson.name}"




