from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from app.job.models import Job
from app.job.forms import JobForm

def index(request):
    return render(request, 'base/index.html')

class JobCreate(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'job/job_form.html'
    success_url = reverse_lazy('job_list')

class JobList(ListView):
    model = Job
    template_name = 'job/job_list.html'

class JobUpdate(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job/job_form.html'
    success_url = reverse_lazy('job_list')

class JobDelete(DeleteView):
    model = Job
    template_name = 'job/job_delete.html'
    success_url = reverse_lazy('job_list')