from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from eajforms.core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.dashboard, name='home'),
    url(r'^accounts/login/$', login, name='login', kwargs={'redirect_authenticated_user': True}),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^dashboard/$', core_views.dashboard, name='dashboard'),
    url(r'', include('eajforms.forms.urls')),
    url(r'', include('eajforms.core.urls'))
]
