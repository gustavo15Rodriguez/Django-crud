from app.proyect.models import Project

from django import forms

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'proj_num',
            'proj_name',
            'proj_value',
            'proj_balance',
            'emp_num',
        ]

        labels = {
            'proj_num': 'Number',
            'proj_name': 'Project Name',
            'proj_value': 'Value',
            'proj_balance': 'Balance',
            'emp_num': 'Employee Number',
        }

        widgets = {
            'proj_num': forms.TextInput(attrs={'class': 'form_control'}),
            'proj_name': forms.TextInput(attrs={'class': 'form_control'}),
            'proj_value': forms.TextInput(attrs={'class': 'form_control'}),
            'proj_balance': forms.TextInput(attrs={'class': 'form_control'}),
            'emp_num': forms.Select(attrs={'class': 'form_control'}),
        }