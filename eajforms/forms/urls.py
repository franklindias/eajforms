from django.conf.urls import url
from eajforms.forms import views as forms_views

urlpatterns = [
    url(r'^form/new/$', forms_views.new, name='new_form')
]
