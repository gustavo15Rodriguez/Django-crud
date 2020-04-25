from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from app.assignmet.models import Assignmet
from app.assignmet.forms import AssignmetForm

class AssignmetCreate(CreateView):
    model = Assignmet
    form_class = AssignmetForm
    template_name = 'assignmet/assignmet_form.html'
    success_url = reverse_lazy('assignmet_list')

class AssignmetList(ListView):
    model = Assignmet
    template_name = 'assignmet/assignmet_list.html'

class AssignmetUpdate(UpdateView):
    model = Assignmet
    form_class = AssignmetForm
    template_name = 'assignmet/assignmet_form.html'
    success_url = reverse_lazy('assignmet_list')

class AssignmetDelete(DeleteView):
    model = Assignmet
    template_name = 'assignmet/assignmet_delete.html'
    success_url = reverse_lazy('assignmet_list')

def index(request):
    return render(request, 'base/index.html')