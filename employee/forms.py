from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_code','nom_complet','telephone','position')
        labels = {
            'emp_code': 'Code',
            'nom_complet': 'Nom complet',
            'telephone': 'Telephone',
            'position': 'Position'
        }


