from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.http import HttpResponseNotFound
from django.utils.deprecation import MiddlewareMixin

class Custom404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Verifica si la respuesta es un 404
        if response.status_code == 404:
            # Llama a la vista personalizada
            from users.views import pre_404_view
            return pre_404_view(request)
        return response
