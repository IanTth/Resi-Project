from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'login_admin', views.Login, name='login'),
    url(r'logout_admin', views.logout_admin, name='logout_admin'),
    url(r'paciente', views.paciente, name='paciente'),
    url(r'consulta', views.consulta, name='consulta'),
    url(r'doctor', views.medico, name='doctor'),
    url(r'home', views.home, name='home'),
    url(r'', views.index, name='index'),


] + static(settings.STATIC_URL)