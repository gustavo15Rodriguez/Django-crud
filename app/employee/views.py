from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from app.employee.models import Employee
from app.employee.forms import EmployeeForm

class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeList(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'

class EmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee/employee_delete.html'
    success_url = reverse_lazy('employee_list')

def index(request):
    return render(request, 'base/index.html')