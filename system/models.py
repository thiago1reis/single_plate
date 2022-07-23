from django.db import models

# Create your models here.
class Owner(models.Model):
    SEX_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Maculino', 'Maculino'),
        ('Outro', 'Outro')
    ]
    STATE_CHOICES = [
        ('Tocantins', 'Tocantins'),
    ]
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, blank=False, null=False)
    cpf = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    zip_code = models.CharField(max_length=255)
    state = models.CharField(max_length=15, choices=STATE_CHOICES, blank=False, null=False)
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
    state = models.CharField(max_length=255)
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
    type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

class Register(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    status = models.BooleanField()
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)


