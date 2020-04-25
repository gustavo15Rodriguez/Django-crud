from django import forms
from app.employee.models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            'emp_num',
            'emp_lname',
            'emp_fname',
            'emp_initial',
            'emp_hiredate',
            'job_code',
            'emp_years',
        ]

        labels = {
            'emp_num': 'Number',
            'emp_lname': 'Last Name',
            'emp_fname': 'First Name',
            'emp_initial': 'Initial',
            'emp_hiredate': 'Date',
            'job_code': 'Job Code',
            'emp_years': 'years',
        }

        widgets = {
            'emp_num': forms.TextInput(attrs={'class': 'form_control'}),
            'emp_lname': forms.TextInput(attrs={'class': 'form_control'}),
            'emp_fname': forms.TextInput(attrs={'class': 'form_control'}),
            'emp_initial': forms.TextInput(attrs={'class': 'form_control'}),
            'emp_hiredate': forms.TextInput(attrs={'class': 'form_control'}),
            'job_code': forms.Select(attrs={'class': 'form_control'}),
            'emp_years': forms.TextInput(attrs={'class': 'form_control'}),
        }