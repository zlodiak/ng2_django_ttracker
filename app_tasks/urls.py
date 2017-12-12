from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^all_statuses$', views.all_statuses, name='all_statuses'),
    url(r'^user_tasks$', views.user_tasks, name='user_tasks'),
    url(r'^get_task$', views.get_task, name='get_task'),
    url(r'^update_task$', views.update_task, name='update_task'),
    url(r'^update_status$', views.update_status, name='update_status'),
]