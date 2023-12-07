from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    body = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body
    
    

