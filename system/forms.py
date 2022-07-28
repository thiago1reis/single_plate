from django import forms
from system.models import Owner, Vehicle

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = ('created', 'modified', 'address_id')
        widgets = {
            'name': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe o nome' ,'autofocus': ''}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}), 
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'cpf': forms.TextInput( attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telephone': forms.TextInput( attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'email': forms.EmailInput( attrs={'class': 'form-control', 'placeholder': 'nome@email.com'}),
            'zip_code': forms.TextInput( attrs={'class': 'form-control', 'placeholder': '00000-000'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'city': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe a cidade'}),
            'district': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe o bairro'}),
            'road': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe a rua'}),
            'number': forms.NumberInput( attrs={'class': 'form-control', 'placeholder': 'Informe o número da casa'}),
            'complement': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe o complemento'}),
            'reference_point': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe um ponto de referência'}),
            'comments': forms.Textarea( attrs={'class': 'form-control', 'style': 'height: 100px'})
        }
        labels = {
            'name': "",
            'birth_date': "",
            'sex': "",
            'cpf': "",
            'telephone': "",
            'email': "",
            'zip_code': "",
            'state': "",
            'city': "",
            'district': "",
            'road': "",
            'number': "",
            'complement': "",
            'reference_point': "",
            'comments': ""
        }
 
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('created', 'modified')
        widgets = {
            'brand_vehicle': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe a marca do veículo' ,'autofocus': ''}),
            'model_vehicle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o modelo do veículo'}), 
            'model_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Informe o ano modelo do veículo'}), 
            'year_manufacture': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Informe o ano de fabricação do veículo'}), 
            'chassis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o chassi do veículo'}), 
            'type': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe a cor do veículo'}), 
        }
        labels = {
            'brand_vehicle': "",
            'model_vehicle': "",
            'model_year': "",
            'year_manufacture': "",
            'chassis': "",
            'type': "",
            'color': ""
        }


   
  
   
