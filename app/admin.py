from django.contrib import admin

# Register your models here.
from .models import Room, Message


@admin.register(Message)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'time_stamp', 'owner', 'room']
    
    
@admin.register(Room)
class RoomModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']