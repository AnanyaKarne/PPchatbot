from django.contrib import admin
from .models import ChatSession
from .models import ChatMessage
admin.site.register(ChatSession)
admin.site.register(ChatMessage)