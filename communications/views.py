from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from .forms import MessageForm


@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('communications:inbox')
    else:
        form = MessageForm()
    return render(request, 'communications/send_message.html', {'form': form})


@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'communications/inbox.html', {'messages': messages})



@login_required
def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'communications/chat_list.html', {'chats': chats})

@login_required
def chat_detail(request, pk):
    chat = get_object_or_404(Chat, pk=pk, participants=request.user)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user
            message.save()
            return redirect('chat_detail', pk=chat.pk)
    else:
        form = MessageForm()
    messages = chat.messages.all()
    return render(request, 'communications/chat_detail.html', {'chat': chat, 'messages': messages, 'form': form})
