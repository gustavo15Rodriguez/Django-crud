from django import forms

from app.job.models import Job

class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            'job_code',
            'job_description',
            'job_chg_hour',
            'job_last_update',
        ]

        labels = {
            'job_code': 'Job Code',
            'job_description': 'Description',
            'job_chg_hour': 'Job Chg Hour',
            'job_last_update': 'Last Update',
        }

        widgets = {
            'job_code': forms.TextInput(attrs={'class': 'form_control'}),
            'job_description': forms.TextInput(attrs={'class': 'form_control'}),
            'job_chg_hour': forms.TextInput(attrs={'class': 'form_control'}),
            'job_last_update': forms.TextInput(attrs={'class': 'form_control'}),
        }