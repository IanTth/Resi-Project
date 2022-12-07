from django.db import models

class Doctor(models.Model):
    nome = models.CharField(max_length=50)
    espec = models.CharField(max_length=50)
    cpf = models.IntegerField()
    crm = models.IntegerField()
    tel = models.IntegerField()

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    cpf = models.IntegerField()
    tel = models.IntegerField(null=True)
    nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.Doctor.nome + "__"+self.Paciente.nome
        