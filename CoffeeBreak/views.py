from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model,
    )
from .forms import UserForm, UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):#isso aqui tá bem errado, é pra mudar
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('postLoginView')
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'CoffeeBreak/loginV2.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            novo_usuario = User.objects.create_user(**form.cleaned_data)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'CoffeeBreak/cadastro.html', {'form': form})

def loginView(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
    else:
        form = UserLoginForm()
    #return render(request, 'CoffeeBreak/loginV2.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('index')

def postLoginView(request):
    return render(request,'CoffeeBreak/dashboard.html')
