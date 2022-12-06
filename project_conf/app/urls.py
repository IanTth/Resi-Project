from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'admin_login/', views.login_admin, name='login_admin'),
    url(r'logout/', views.logout_admin, name='logout_admin'),
    url(r'paciente/', views.paciente, name='paciente'),
    url(r'consulta/', views.consulta, name='consulta'),
    url(r'doctor/', views.medico, name='doctor'),
    url(r'', views.home, name='home'),

] + static(settings.STATIC_URL)