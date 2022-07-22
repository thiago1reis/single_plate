from django import forms
from system.models import Owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = ('created', 'modified', 'address_id')
        widgets = {
            'name': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Informe o nome' ,'autofocus': ''}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}), 
        }
        labels = {
            'name': "",
            'birth_date': "",
        }
 

