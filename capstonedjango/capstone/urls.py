from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.contrib import admin
import django.contrib.auth.views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
