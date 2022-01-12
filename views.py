from django.shortcuts import redirect, render, HttpResponse
from AppCoder.models import PosibleJugador
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppCoder.models import Jugador, PosibleJugador
from AppCoder.forms import UserRegisterForm, UserEditForm

# Create your views here.

def inicio(request):
    
      
    return render(request, "AppCoder/inicio.html")

@login_required
def posibleJugador(request):
    
    if request.method == "POST":
        
             
        posibleJugador = PosibleJugador(apellido = request.POST['apellido'], numero = request.POST['numero'], edad = request.POST['edad'], equipo = request.POST['equipo'])
        
        posibleJugador.save()
        
        return render(request, "AppCoder/posibleJugador.html")
    return render(request, 'AppCoder/posibleJugador.html')

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                
                login(request, user)
                return render(request, 'AppCoder/inicio.html', { "mensaje" : f"Bienvenido {usuario}" })
            
            else:
                return render(request, 'AppCoder/inicio.html', { "mensaje" : f"Datos incorrectos" })
            
        else:
            return render(request, 'AppCoder/inicio.html', { "mensaje" : f"Formulario erroneo" })
                
                    
    form = AuthenticationForm()
    
    return render(request, "AppCoder/login.html",{"form": form})


def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f'Usuario {username} Creado'})
    else:
        form = UserRegisterForm()
    return render(request, "AppCoder/register.html" , {'form':form})
    
  


@login_required
def leerPosiblesJugadores(request):
    
    PosiblesJugadores = PosibleJugador.objects.all()
        
    dir = {'PosiblesJugadores' : PosiblesJugadores}
        
    return render(request, "AppCoder/leerPosiblesJugadores.html", dir)

@login_required
def leerPosiblesJugadoresDetalles(request):
    
    PosiblesJugadores = PosibleJugador.objects.all()
        
    dir = {'PosiblesJugadores' : PosiblesJugadores}
    
    return render(request, "AppCoder/leerPosiblesJugadoresDetalles.html", dir)



def about(request):
    return render(request, "AppCoder/about.html")

@login_required
def editarUsuario(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion =  miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 =  informacion['password1']
            usuario.password2 =  informacion['password2']
            
            
            usuario.save()

            return render(request, "AppCoder/inicio.html")
        
    else: 
            
       miFormulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, "AppCoder/editarUsuario.html", {'miFormulario': miFormulario, 'usuario': usuario})
            