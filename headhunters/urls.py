

from django.urls import path
from .views import (
    JobOfferListView, JobOfferDetailView, JobOfferCreateView, JobOfferUpdateView, JobOfferDeleteView,
    HeadhunterListView, HeadhunterDetailView, HeadhunterCreateView, HeadhunterUpdateView, HeadhunterDeleteView,
    ScheduleListView, ScheduleDetailView, ScheduleCreateView, ScheduleUpdateView, ScheduleDeleteView, get_candidates,
    LandingHeadHuntersView,ManageCandidatesView,
    CreateOfferView,
    AddToExistingOfferView,
    
)


urlpatterns = [
    path('joboffers/', JobOfferListView.as_view(), name='joboffer_list'),
    path('joboffers/<int:pk>/', JobOfferDetailView.as_view(), name='joboffer_detail'),
    path('joboffers/create/', CreateOfferView.as_view(), name='joboffer_create'),
    path('joboffers/<int:pk>/update/', JobOfferUpdateView.as_view(), name='joboffer_update'),
    path('joboffers/<int:pk>/delete/', JobOfferDeleteView.as_view(), name='joboffer_delete'),

    path('headhunters/', HeadhunterListView.as_view(), name='headhunter_list'),
    path('headhunters/<int:pk>/', HeadhunterDetailView.as_view(), name='headhunter_detail'),
    path('headhunters/create/', HeadhunterCreateView.as_view(), name='headhunter_create'),
    path('headhunters/<int:pk>/update/', HeadhunterUpdateView.as_view(), name='headhunter_update'),
    path('headhunters/<int:pk>/delete/', HeadhunterDeleteView.as_view(), name='headhunter_delete'),
    
    path('schedule/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedule/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    
    
    path('schedule/<int:pk>/update/', ScheduleUpdateView.as_view(), name='schedule_update'),
    path('schedule/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
    path("landing/", LandingHeadHuntersView.as_view(), name="landing_headhunters"),
    
     #Rutas para gestion de candidatos en la landing
     #
      path('manage_candidates/', ManageCandidatesView.as_view(), name='manage_candidates'),
    #Ruta para crear oferta desde seleccionados
      path('create_offer/<str:candidate_ids>/', CreateOfferView.as_view(), name='create_offer'),
      path('add_to_existing_offer/<str:candidate_ids>/', AddToExistingOfferView.as_view(), name='add_to_existing_offer'),
      path('get-candidates/<int:joboffer_id>/', get_candidates, name='get_candidates'),
     
   
]
