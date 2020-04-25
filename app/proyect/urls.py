from django.conf.urls import url

from app.proyect.views import index, ProjectCreate, ProjectList, ProjectUpdate, ProjectDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', ProjectCreate.as_view(), name='project_create'),
    url(r'^list$', ProjectList.as_view(), name='project_list'),
    url(r'^edit(?P<pk>[\d]+)/$', ProjectUpdate.as_view(), name='project_edit'),
    url(r'^delete(?P<pk>[\d]+)/$', ProjectDelete.as_view(), name='project_delete'),
]