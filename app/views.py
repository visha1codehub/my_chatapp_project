from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from .models import Room, Message


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("<h1>Invalid User!!!!</h1>")
    return render(request, 'app/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("<h1>Invalid Inputs!!!!</h1>")
    context = {'form': form}
    return render(request, 'app/register.html', context)

def home(request):
    if request.method == 'POST':
        roomName = request.POST['roomName']
        return redirect('room', roomName=roomName)
    return render(request, "app/index.html", {})

@login_required(login_url='login')
def room(request, roomName):
    room, created = Room.objects.get_or_create(name=roomName)
    messages = [] if created else room.message_set.all()
    context = {'roomName':roomName, 'messages':messages}     
    return render(request, 'app/room.html', context)
