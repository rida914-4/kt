from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'cashflow/$', views.mis, name='mis'),
    url(r'invest/$', views.mis, name='mis'),
]