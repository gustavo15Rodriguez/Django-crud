from django.conf.urls import url

from app.assignmet.views import index, AssignmetCreate, AssignmetList, AssignmetUpdate, AssignmetDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', AssignmetCreate.as_view(), name='assignmet_create'),
    url(r'^list$', AssignmetList.as_view(), name='assignmet_list'),
    url(r'^edit/(?P<pk>[\d]+)/$', AssignmetUpdate.as_view(), name='assignmet_edit'),
    url(r'^eliminate/(?P<pk>[\d]+)/$', AssignmetDelete.as_view(), name='assignmet_delete'),
]