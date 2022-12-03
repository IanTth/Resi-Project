from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'home', views.home, name='home'),
    url(r'', views.login, name='login' ),

] + static(settings.STATIC_URL)