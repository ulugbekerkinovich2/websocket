from django.contrib import admin

from chat.models import Conversation, Message, Message_NEW, Conversation_NEW

# Register your models here.
admin.site.register(Conversation)
admin.site.register(Conversation_NEW)
admin.site.register(Message)
admin.site.register(Message_NEW)
admin.site.site_header = 'Chat Admin'
admin.site.site_title = 'Chat Admin Portal'
admin.site.index_title = 'Welcome to Chat Admin Portal'

