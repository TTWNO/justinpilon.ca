from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

from . import forms

# Create your views here.
def index(request):
    return render(request, 'justinpilon/index.html', {})

def pdfs(request):
    return render(request, 'justinpilon/pdfs.html', {})

def chat(request):
    return render(request, 'justinpilon/chat.html', {})

def room(request, room_name):
    return render(request, 'justinpilon/room.html', {
        'room_name': room_name
    })

class SignUp(generic.CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'