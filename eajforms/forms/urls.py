from django.conf.urls import url
from eajforms.forms import views as forms_views

urlpatterns = [
    url(r'^form/new/$', forms_views.form_new, name='form_new'),
    url(r'^form/save/$', forms_views.form_save, name='form_save'),
    url(r'^form/list/$', forms_views.form_list, name='form_list'),
    url(r'^form/(?P<pk>\d+)/apply/$', forms_views.form_apply, name='form_apply'),
    url(r'^apply_form/(?P<access_code>\w+)/response/$', forms_views.form_response, name='form_response'),
    url(r'^apply_form/response/save/$', forms_views.form_response_save, name='form_response_save'),
    url(r'^apply_form/list/$', forms_views.apply_form_list, name='apply_form_list'),
    url(r'^apply_form/(?P<access_code>\w+)/result/$', forms_views.apply_form_result, name='apply_form_result'),
]