from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsuarioForm
from django.shortcuts import redirect

# Create your views here.
def index(request):#isso aqui tá bem errado, é pra mudar
    return render(request, 'CoffeeBreak/base.html')

def post_new(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'CoffeeBreak/new_user.html', {'form': form})
