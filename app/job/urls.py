from django.conf.urls import url

from app.job.views import index, JobCreate, JobList, JobUpdate, JobDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', JobCreate.as_view(), name='job_create'),
    url(r'^list$', JobList.as_view(), name='job_list'),
    url(r'^edit/(?P<pk>[\d]+)/$', JobUpdate.as_view(), name='job_edit'),
    url(r'^delete/(?P<pk>[\d]+)/$', JobDelete.as_view(), name='job_delete'),
]