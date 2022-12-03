from django.db import models

class Doctor(models.Model):
    nome = models.CharField(max_length=50)
    espec = models.CharField(max_length=50)
    cpf = models.IntegerField()
    crm = models.IntegerField()
    tel = models.IntegerField()

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    endereço = models.TextField
    genero = models.CharField(max_length=10)
    cpf = models.IntegerField()
    tel = models.IntegerField(null=True)


class Consulta(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()