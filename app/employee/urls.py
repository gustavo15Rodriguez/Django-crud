from django.conf.urls import url
from app.employee.views import index, EmployeeCreate, EmployeeList, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', EmployeeCreate.as_view(), name='employee_create'),
    url(r'^list$', EmployeeList.as_view(), name='employee_list'),
    url(r'^edit/(?P<pk>[\d]+)/$', EmployeeUpdate.as_view(), name='employee_edit'),
    url(r'^eliminate/(?P<pk>[\d]+)/$', EmployeeDelete.as_view(), name='employee_delete'),
]
