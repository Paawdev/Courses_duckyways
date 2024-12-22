from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from gaming.models import DuckyCoin
from .models import Message
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.dateparse import parse_date


@login_required
def search_users(request):
    query = request.GET.get('q', '')  # Obtén el texto ingresado
    if query:
        users = User.objects.filter(Q(username__icontains=query)).exclude(id=request.user.id)[:10]  # Excluir al usuario actual
        results = [{'id': user.id, 'username': user.username} for user in users]
    else:
        results = []
    return JsonResponse(results, safe=False)

@login_required
def inbox(request):
    
    #Mensajes recibidos activos
    messages = Message.objects.filter(
        recipient=request.user,  # Usuario autenticado como destinatario
        is_active=True           # Solo mensajes activos
    ).order_by('-timestamp')

    # Mensajes ocultos (opcional)
    hidden_messages = Message.objects.filter(
        recipient=request.user,
        is_active=False          # Mensajes marcados como inactivos
    ).order_by('-timestamp')

    # Aplicar Filtros
    sender_username = request.GET.get('sender', '').strip()
    search_query = request.GET.get('search', '').strip()
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    status = request.GET.get('status', '').strip()

    # Filtrar por remitente
    if sender_username:
        messages = messages.filter(sender__username__icontains=sender_username)

    # Filtrar por búsqueda en asunto o contenido
    if search_query:
        messages = messages.filter(
            Q(subject__icontains=search_query) | Q(body__icontains=search_query)
        )

    # Filtrar por intervalo de fechas
    if start_date:
        start_date = parse_date(start_date)
        if start_date:
            messages = messages.filter(timestamp__date__gte=start_date)
    if end_date:
        end_date = parse_date(end_date)
        if end_date:
            messages = messages.filter(timestamp__date__lte=end_date)

    # Filtrar por estado (leído/no leído)
    if status == 'read':
        messages = messages.filter(is_read=True)
    elif status == 'unread':
        messages = messages.filter(is_read=False)
    return render(request, 'messaging/inbox.html', {
        'messages': messages,
        'hidden_messages': hidden_messages
    })


@login_required
def deactivate_message(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    if request.method == "POST":
        message.is_active = False
        message.save()
        messages.success(request, "Message deactivated successfully.")
        return redirect('inbox')
    return render(request, 'messaging/deactivate_message.html', {'message': message})


@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messaging/sent.html', {'messages': messages})

from django.http import HttpResponseRedirect

@login_required
def view_message(request, pk):
    # Obtener el mensaje
    message = get_object_or_404(Message, pk=pk)

    # Cambiar el estado a leído solo si el usuario es el destinatario
    if message.recipient == request.user and not message.is_read:
        message.is_read = True
        message.save()

    # Manejar el formulario de respuesta
    if request.method == "POST":
        response_body = request.POST.get('response_body')
        if response_body:
            # Crear una respuesta vinculada al mensaje original
            Message.objects.create(
                sender=request.user,
                recipient=message.sender,
                subject=f"Re: {message.subject}",
                body=response_body,
                reply_to=message  # Vincula esta respuesta al mensaje original
            )
            messages.success(request, "Your reply has been sent.")
            return HttpResponseRedirect(request.path_info)

    return render(request, 'messaging/view_message.html', {'message': message})


@login_required
def send_message(request):
    if request.method == "POST":
        receiver_username = request.POST.get('receiver')  # Obtén el destinatario del formulario
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        try:
            # Busca el usuario destinatario
            receiver = User.objects.get(username=receiver_username)
            # Crea el mensaje con el campo 'recipient' correcto
            Message.objects.create(sender=request.user, recipient=receiver, subject=subject, body=body)
            messages.success(request, "Message sent successfully! +5 DuckyCoins earned.")
          # Obtener o crear los DuckyCoins del remitente
            duckycoin, created = DuckyCoin.objects.get_or_create(user=request.user)
            amount = 3 # Cantidad de DuckyCoins a incrementar
            application = "Messages"  # Nombre de la aplicación
            description = "DuckyCoins por envio de mensaje."  # Descripción

            duckycoin.add_coins(amount, application, description)

            
            return redirect('inbox')
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('send_message')

    return render(request, 'messaging/send_message.html')

@login_required
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    if request.method == "POST":
        message.delete()
        messages.success(request, "Message permanently deleted.")
        return redirect('inbox')
    
@login_required
def reactivate_message(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    if request.method == "POST":
        message.is_active = True
        message.save()
        messages.success(request, "Message reactivated successfully.")
        return redirect('inbox')
