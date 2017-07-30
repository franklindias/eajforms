from django.conf.urls import url
from . import views as core_views

urlpatterns = [
    url(r'^class/list/$', core_views.class_list, name='class_list'),
    url(r'^class/(?P<pk>\d+)/matriculations/$', core_views.class_matriculations, name='class_matriculations'),
    url(r'^class/matriculation/upload$', core_views.class_matriculation_upload, name='class_matriculation_upload'),
]