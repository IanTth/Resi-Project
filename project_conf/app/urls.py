from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from .views import *

"""urlpatterns = [
    url(r'login_admin', views.Login, name='login'),
    url(r'logout_admin', views.logout_admin, name='logout_admin'),
    url(r'paciente', views.paciente, name='paciente'),
    url(r'consulta', views.consulta, name='consulta'),
    url(r'doctor', views.doctor, name='doctor'),
    url(r'delete_doctor', views.del_doctor, name='del_doctor'),
    url(r'home', views.home, name='home'),
    url(r'', views.index, name='index'),



] + static(settings.STATIC_URL)"""


urlpatterns = [
    path('', index, name='index'),
    path('doctor/', doctor, name='doctor'),
    path('del_doctor(?P<int:pid>)/', del_doctor, name='del_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),

    path('login/', Login, name='login'),
    path('logout/', logout, name='logout_admin'),
    path('paciente/', paciente, name='paciente'),
    path('consulta/', consulta, name='consulta'),
    path('home/', home, name='home'),

] + static(settings.STATIC_URL)