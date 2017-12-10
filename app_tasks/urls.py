from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^all_statuses$', views.all_statuses, name='all_statuses'),
]