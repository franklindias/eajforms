from django.conf.urls import url
from . import views as core_views

urlpatterns = [
    url(r'^class/list/$', core_views.class_list, name='class_list'),
    url(r'^class/(?P<pk>\d+)/matriculations/$', core_views.class_matriculations, name='class_matriculations'),
    url(r'^class/matriculation/upload$', core_views.class_matriculation_upload, name='class_matriculation_upload'),

    url(r'^docente/list/$', core_views.docente_list, name='docente_list'),
    url(r'^docente/upload/$', core_views.docente_upload, name='docente_upload'),

    url(r'^course/list/$', core_views.course_list, name='course_list'),

    url(r'^avaluated/load/$', core_views.load_avaluated_by_type, name='load_avaluated_by_type'),
]