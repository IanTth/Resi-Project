from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .models import *


def index(request): 
    
    return render(request,'index.html')

def home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'home.html')




def Login(request):
    error = ""
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        user = authenticate(username=cpf, password = senha)
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




def doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'doctor.html', d)

def del_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(crm=pid)
    doctor.delete()
    return redirect('doctor')

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        nome = request.POST['nome']
        espec = request.POST['espec']
        cpf = request.POST['cpf']
        crm = request.POST['crm']
        tel = request.POST['tel']
    
        try:
            Doctor.objects.create(nome=nome, espec=espec, cpf=cpf, crm=crm, tel=tel)
            error = 'no'

        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'doctor.html', d)






def consulta(request): 
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'consulta.html')

