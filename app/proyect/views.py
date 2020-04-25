from django.shortcuts import render

from app.proyect.forms import ProjectForm
from app.proyect.models import Project
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

def index(request):
    return render(request, 'base/index.html')

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectList(ListView):
    model = Project
    template_name = 'project/project_list.html'

class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDelete(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('project_list')