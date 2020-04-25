from django import forms

from app.assignmet.models import Assignmet

class AssignmetForm(forms.ModelForm):

    class Meta:
        model = Assignmet

        fields = [
            'assign_num',
            'assign_date',
            'proj_num',
            'emp_num',
            'assign_job',
            'assign_chg_hr',
            'assign_hours',
            'assign_charge',
        ]

        labels = {
            'assign_num': 'Assignmet Number',
            'assign_date': 'Assignmet Date',
            'proj_num': 'Project Number',
            'emp_num': 'Employee Number',
            'assign_job': 'Assignmet Job',
            'assign_chg_hr': 'Assignmet chg hours',
            'assign_hours': 'Assignmet hours',
            'assign_charge': 'Assignmet charge',
        }

        widgets = {
            'assign_num': forms.TextInput(attrs={'class': 'form_control'}),
            'assign_date': forms.TextInput(attrs={'class': 'form_control'}),
            'proj_num': forms.TextInput(attrs={'class': 'form_control'}),
            'emp_num': forms.Select(attrs={'class': 'form_control'}),
            'assign_job': forms.TextInput(attrs={'class': 'form_control'}),
            'assign_chg_hr': forms.TextInput(attrs={'class': 'form_control'}),
            'assign_hours': forms.TextInput(attrs={'class': 'form_control'}),
            'assign_charge': forms.TextInput(attrs={'class': 'form_control'}),
        }