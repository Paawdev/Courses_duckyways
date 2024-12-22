from django.urls import path
from .views import *

app_name = "courses"

urlpatterns = [
    # ----------- Course URL patterns --------------
    path('courses/', courses_list_view, name='courses-list'),                                    # List courses
    path('courses/<int:course_id>/', course_detail_view, name='course-detail'),                  # Read course
    path('courses/add/', course_create_or_update_view, name='course-create'),                    # Create course
    path('courses/<int:course_id>/edit/', course_create_or_update_view, name='course-update'),   # Update course
    path('courses/<int:course_id>/delete/', course_delete_view, name='course-delete'),           # Delete course

    # ----------- Course_User URL patterns --------------
    path('courses/user/', course_user_list_view, name='course-user-list'),                              # List user courses
    path('courses/<int:course_id>/user/', course_user_detail_view, name='course-user-detail'),          # Read course_user
    path('courses/<int:course_id>/enroll_user/', course_enroll_user_view, name='course-enroll-user'),   # Enroll User in course
    path('courses/<int:course_id>/complete_course/', course_complete_view, name='course-complete'),     # Course completion

    # ----------- Teacher URL patterns --------------
    path('teacher/courses/<int:course_id>/', course_teacher_detail_view, name='teacher-course-detail'),  # Read/Edit course_teacher
    path('teacher/courses/', course_teacher_list_view, name='teacher-course-list'),                      # List course_teacher
    path('teacher/profile/add', teacher_profile_create_or_update_view, name='teacher-profile-create'),   # Create profile_teacher

    # ----------- Module URL patterns --------------
    path('courses/<int:course_id>/module/add/', module_create_or_update_view, name='module-create'),                # Create module
    path('courses/<int:course_id>/module/<int:module_id>/', module_create_or_update_view, name='module-update'),    # Update module
    path('courses/<int:course_id>/module/<int:module_id>/delete/', module_delete_view, name='module-delete'),       # Delete module

    # ----------- Lesson URL patterns --------------
    path('courses/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/', lesson_detail_view, name='lesson-detail'),                     # Read lesson
    path('courses/<int:course_id>/module/<int:module_id>/lesson/add/', lesson_create_or_update_view, name='lesson-create'),                    # Create lesson
    path('courses/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/edit/', lesson_create_or_update_view, name='lesson-update'),   # Update lesson
    path('courses/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/delete/', lesson_delete_view, name='lesson-delete'),           # Delete lesson

    # ----------- Resource_Course URL patterns --------------
    path('courses/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/resource/add/',
        resource_course_create_or_update_view,
        name='resource-course-create'                                                                                           # Create resource
    ),
    path('courses/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/resource/<int:resource_id>/edit/', 
        resource_course_create_or_update_view,
        name='resource-course-update'                                                                                           # Update resource
    ),
    path('courses/<int:course_id>/module/<int:module_id>/lesson/<int:lesson_id>/resource/<int:resource_id>/delete/',
        resource_course_delete_view,
        name='resource-course-delete'                                                                                           # Delete resource
    ),

    # ----------- Certificate URL patterns --------------
    path('courses/<int:course_id>/certificate/add/', certificate_create_or_update_view, name='certificate-create'),                     # Create
    path('courses/<int:course_id>/certificate/<int:certificate_id>/', certificate_create_or_update_view, name='certificate-update'),    # Update
    path('courses/<int:course_id>/certificate/<int:certificate_id>/delete/', certificate_delete_view, name='certificate-delete'),       # Delete

    # ----------- Resources URL patterns --------------
    path('resources/', resources_list_view, name = 'resources-list'),  # List resources

    # ----------- Review URL patterns ---------------
    path('courses/<int:course_id>/review/', create_or_update_course_review_view, name = 'review-course-create'),
    path('courses/<int:course_id>/review/<int:review_id>/', create_or_update_course_review_view, name ='review-course-update'),
    # path('resources/<int:course_id>/review/', create_or_update_resource_review_view, name = 'review-resource-create'),
    # path('resources/<int:course_id>/review/<int:review_id>', create_or_update_resource_review_view, name ='review-resource-update'),

    # ------------ Wishlist URL patterns -------------
    path('courses/<int:course_id>/add_wish/', add_userwish_view, name = 'add-userwish'), # Add

    # ----------- Chatbot URL patterns --------------
    path('courses/chatbot/', chat_view, name='chatbot'),
]