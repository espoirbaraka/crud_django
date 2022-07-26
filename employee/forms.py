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

    def __int__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False

