from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
from .models import Room, Message
import json


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['roomName']
        print("Connected!!!")
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
        
    async def receive(self, text_data=None, bytes_data=None):
        print("Received from client:", text_data)
        room = await database_sync_to_async(Room.objects.get)(name=self.room_name)
        # print(type(room), room)
        user = self.scope['user']
        data = json.loads(text_data)
        body = data['msg']
        message = Message(body=body, owner=user, room=room)
        await database_sync_to_async(message.save)()
        data['user'] = user.username
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type' : 'chat.message',
                'message' : json.dumps(data)
            }
        )
        
    async def chat_message(self, event):
        await self.send(text_data=event['message'])
        
    async def disconnect(self, code):
        print("Websocket Disconnected!!!", code)
        raise StopConsumer()