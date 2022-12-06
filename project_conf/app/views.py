from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout


def home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'home.html')

def login_admin(request):
    error = ""
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        user = authenticate(username=login, password = senha)
        try:
            if user.is_staff:
                login(request,user)
                error = "N"
            else:
                error= "Y"
        except:
            error = "Y"
    d = {'error':error}
    return render(request,'login_admin.html', d)
    
def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')





def paciente(request): 
    return render(request,'paciente.html')

def medico(request): 
    return render(request,'doctor.html')

def consulta(request): 
    return render(request,'consulta.html')

