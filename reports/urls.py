from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.reports, name='reports'),
    url(r'^(?P<file_name>\w+)$', views.pf_pl_invoicedet, name='pf_pl_invoicedet'),
    url(r'rdownload', views.reports_download),

]
