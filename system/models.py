from django.db import models

# Create your models here.
STATE_CHOICES = [
        ('Acre', 'Acre'),
        ('Alagoas', 'Alagoas'),
        ('Amazonas', 'Amazonas'),
        ('Bahia', 'Ceará'),
        ('Distrito Federal', 'Distrito Federal'),
        ('Espírito Santo', 'Espírito Santo'),
        ('Goiás', 'Goiás'),
        ('Maranhão', 'Maranhão'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
        ('Minas Gerais', 'Minas Gerais'),
        ('Pará', 'Pará'),
        ('Paraíba', 'Paraíba'),
        ('Paraná', 'Paraná'),
        ('Pernambuco', 'Pernambuco'),
        ('Piauí', 'Piauí'),
        ('Rio de Janeiro', 'Rio de Janeiro'),
        ('Rio Grande do Norte', 'Rio Grande do Norte'),
        ('Rio Grande do Sul', 'Rio Grande do Sul'),
        ('Rondônia', 'Rondônia'),
        ('Roraima', 'Roraima'),
        ('Santa Catarina', 'Santa Catarina'),
        ('São Paulo', 'São Paulo'),
        ('Sergipe', 'Sergipe'),
        ('Tocantins', 'Tocantins'),
    ]

SEX_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Maculino', 'Maculino'),
        ('Outro', 'Outro')
    ]

TYPE_VEHICLE_CHOICES = [
        ('Automóvel', 'Automóvel'),
        ('Caminhão', 'Caminhão'),
        ('Caminhão trator', 'Caminhão trator'),
        ('Caminhonete', 'Caminhonete'),
        ('Camioneta', 'Camioneta'),
        ('Ciclomotor', 'Ciclomotor'),
        ('Micro-ônibus', 'Micro-ônibus'),
        ('Motocicleta', 'Motocicleta'),
        ('Motoneta', 'Motoneta'),
        ('Ônibus', 'Ônibus'),
        ('Quadriciclo', 'Quadriciclo'),
        ('Reboque', 'Reboque'),
        ('Semirreboque', 'Semirreboque'),
        ('Triciclo', 'Triciclo'),
        ('Utilitário', 'Utilitário')
    ]
    
class Owner(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, blank=False, null=False)
    cpf = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    zip_code = models.CharField(max_length=255)
    state = models.CharField(max_length=25, choices=STATE_CHOICES, blank=False, null=False)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    road = models.CharField(max_length=255)
    number = models.IntegerField(blank=True, null=True)
    complement = models.CharField(max_length=255, blank=True, null=True)
    reference_point = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    def __str__(self):
        return self.nome
class Plate(models.Model):
    state = models.CharField(max_length=25, choices=STATE_CHOICES, blank=False, null=False)
    type = models.CharField(max_length=255)
    three_char = models.CharField(max_length=255)
    only_number = models.IntegerField()
    single_char = models.CharField(max_length=255)
    two_number = models.IntegerField()
    status = models.BooleanField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
   
class Vehicle(models.Model):
    brand_vehicle = models.CharField(max_length=255)
    model_vehicle = models.CharField(max_length=255)
    model_year = models.IntegerField()
    year_manufacture = models.IntegerField()
    chassis = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPE_VEHICLE_CHOICES, blank=False, null=False)
    color = models.CharField(max_length=255)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    def __str__(self):
        return self.nome
class Register(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    status = models.BooleanField()
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)


