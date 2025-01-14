from django.contrib import admin
from .models import Port, Boat, Charter, Photo, Message, Chat

admin.site.register(Port)
admin.site.register(Boat)
admin.site.register(Charter)
admin.site.register(Photo)
admin.site.register(Chat)
admin.site.register(Message)