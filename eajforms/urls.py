from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from .core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^dashboard/$', core_views.dashboard, name='dashboard'),
    url(r'', include('eajforms.forms.urls'))
]
