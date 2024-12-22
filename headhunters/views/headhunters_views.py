

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import HeadHunterUser,JobOffer,ManagementCandidates
from ..forms import HeadHunterForm
from django.shortcuts import render,redirect,get_object_or_404
from profile_cv.models import Profile_CV
from django.views import View



class HeadhunterListView(ListView):
    model = HeadHunterUser
    template_name = 'headhunters/headhunter_list.html'
    context_object_name = 'headhunters'

class HeadhunterDetailView(DetailView):
    model = HeadHunterUser
    template_name = 'headhunters/headhunter_detail.html'
    context_object_name = 'headhunter'

class HeadhunterCreateView(CreateView):
    model = HeadHunterUser
    form_class = HeadHunterForm
    template_name = 'headhunters/headhunter_form.html'
    
    def form_valid(self, form):
        #Guardo el headhunter en la base de datos
        headhunter = form.save()
        #lo redirigo a el detalle del headhunter
        return redirect('headhunter_detail', pk=headhunter.pk)

class HeadhunterUpdateView(UpdateView):
    model = HeadHunterUser
    form_class = HeadHunterForm
    template_name = 'headhunters/headhunter_form.html'
    success_url = reverse_lazy('headhunter_list')

class HeadhunterDeleteView(DeleteView):
    model = HeadHunterUser
    template_name = 'headhunters/headhunter_confirm_delete.html'
    success_url = reverse_lazy('headhunter_list')
    
    
class LandingHeadHuntersView(ListView):
    model = Profile_CV
    template_name = 'headhunters/landing_headhunters.html'
    context_object_name = 'candidates'
    #manejar la paginacion
    paginate_by = 9
    

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener filtros de manera más segura
        location_filter = self.request.GET.get('location', '')
        availability_filter = self.request.GET.get('open_to_work', '')
        vehicle_filter = self.request.GET.get('vehicle', '')
        disability_filter = self.request.GET.get('disability', '')
        disability_percentage_filter = self.request.GET.get('disability_percentage', '')

        # Filtrar por ubicación
        if location_filter:
            queryset = queryset.filter(address__icontains=location_filter)

        # Filtro por disponibilidad
        if availability_filter.lower() in ['true', 'false']:
            queryset = queryset.filter(open_to_work=availability_filter.lower() == 'true')

        # Filtro por vehículo
        if vehicle_filter.lower() in ['true', 'false']:
            queryset = queryset.filter(vehicle=vehicle_filter.lower() == 'true')

        # Filtro por discapacidad
        if disability_filter.lower() in ['true', 'false']:
            queryset = queryset.filter(disability=disability_filter.lower() == 'true')

        # Filtro por porcentaje de discapacidad
        if disability_percentage_filter.isdigit():
            queryset = queryset.filter(disability_percentage__gte=int(disability_percentage_filter))

        return queryset



 #Esta Vista relacionara los candidatos seleccionados con la oferta:


class ManageCandidatesView(View):
    def post(self, request, *args, **kwargs):
        # Obtener los candidatos seleccionados y la acción
        selected_candidates_ids = request.POST.getlist("selected_candidates")
        action = request.POST.get("action")

        # Verificar si se seleccionaron candidatos
        if not selected_candidates_ids:
            return redirect("landing_headhunters")

        candidates = Profile_CV.objects.filter(id__in=selected_candidates_ids)

        # Realizar acción según el valor de 'action'
        if action == "create_offer":
            return redirect("create_offer", candidate_ids=",".join(selected_candidates_ids))

        elif action == "add_to_existing_offer":
            return redirect("add_to_existing_offer", candidate_ids=",".join(selected_candidates_ids))

        return redirect("landing_headhunters")



