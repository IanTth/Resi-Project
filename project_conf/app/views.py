from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .models import *


def index(request): 
    
    return render(request,'index.html')

def home(request):
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    paciente1 = Paciente.objects.all()

    if request.method == 'POST':
        n = request.POST['doctor']
        p = request.POST['paciente']
        da = request.POST['data']
        h = request.POST['hora']

        doctor = Doctor.objects.filter(nome=n).first()
        paciente = Paciente.objects.filter(nome=p).first()

        try:
            Consulta.objects.create(Doctor=doctor, Paciente=paciente, data=da, hora=h)
            return redirect('consulta')
        except:
            error = ""

    con = Consulta.objects.all()
    d = {'con':con,'doctor':doctor1, 'paciente':paciente1}
    return render(request,'home.html',d)



def del_consulta(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    consulta = Consulta.objects.get(id=pid)
    consulta.delete()
    return redirect('consulta')



def Login(request):
    error = ""
    if request.method == 'POST':
        nome = request.POST['nome']
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
    
def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('index')





def paciente(request): 
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        nome = request.POST['nome']
        genero = request.POST['genero']
        cpf = request.POST['cpf']
        nascimento = request.POST['nascimento']
        tel = request.POST['tel']
    
        Paciente.objects.create(nome=nome, genero=genero, cpf=cpf, nascimento=nascimento, tel=tel)
            
        
        return redirect('paciente')

    pac = Paciente.objects.all()
    p = {'pac':pac}
    return render(request,'paciente.html',p)

def del_paciente(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    paciente = Paciente.objects.get(cpf=pid)
    paciente.delete()
    return redirect('paciente')




def doctor(request):
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        nome = request.POST['nome']
        espec = request.POST['espec']
        cpf = request.POST['cpf']
        crm = request.POST['crm']
        tel = request.POST['tel']
    
        Doctor.objects.create(nome=nome, espec=espec, cpf=cpf, crm=crm, tel=tel)
            
        
        return redirect('doctor')


    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'doctor.html', d)

def del_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(cpf=pid)
    doctor.delete()
    return redirect('doctor')







