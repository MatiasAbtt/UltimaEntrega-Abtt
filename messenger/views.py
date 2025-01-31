from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def inbox_view(request):
    # Mensajes recibidos
    messages_inbox = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messenger/inbox.html', {'messages_inbox': messages_inbox})

@login_required
def send_message_view(request):
    if request.method == 'POST':
        receiver_username = request.POST['receiver']
        content = request.POST['content']

        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return render(request, 'messenger/send_message.html', {'error': 'Usuario no encontrado.'})

        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('inbox')

    return render(request, 'messenger/send_message.html')