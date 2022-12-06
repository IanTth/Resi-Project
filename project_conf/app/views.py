from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout


def index(request): 
    
    return render(request,'index.html')

def home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'home.html')

def Login(request):
    error = ""
    if request.method == 'POST':
        nome = request.POST['login']
        senha = request.POST['senha']
        user = authenticate(username=nome, password = senha)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error= "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login_admin.html', d)
    
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def paciente(request): 
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'paciente.html')

def medico(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'doctor.html')

def consulta(request): 
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'consulta.html')



