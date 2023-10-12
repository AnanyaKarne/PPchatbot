from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')  # Redirect to the chat interface after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('chat')  # Redirect to the chat interface after login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



from .models import ChatSession, ChatMessage

def chat(request, session_id):
    # Retrieve the chat session and messages
    chat_session = ChatSession.objects.get(pk=session_id)
    chat_messages = ChatMessage.objects.filter(session=chat_session)

    if request.method == 'POST':
        # Handle message submission here
        message_text = request.POST.get('message')  # Get user input
        sender = request.user

        # Create and save the chat message
        chat_message = ChatMessage(session=chat_session, sender=sender, message=message_text)
        chat_message.save()

        # Redirect back to the chat interface
        return redirect('chat', session_id=session_id)

    return render(request, 'chatbot/chat.html', {
        'chat_session': chat_session,
        'chat_messages': chat_messages,
    })

# Create your views here.
