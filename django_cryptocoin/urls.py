from django.urls import re_path

from .views import process, check_status

app_name = 'django_cryptocoin'
urlpatterns = [
    re_path(r'^process/(?P<addr>.+)$', process, name='cryptocoin-order-process'),
    re_path(r'^check_status/(?P<addr>.+)$', check_status, name='cryptocoin-order-check-status'),
]