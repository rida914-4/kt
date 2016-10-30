from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'party_trial/$', views.party_trial, name='party_trial'),
    url(r'party_trial/(?P<party_id>\w+\d+)$', views.party_trial_detail_w, name='party_trial_detail'),
    url(r'party_trial/(?P<party_id>\w+\d+)_(?P<date_from>(\d+\-\d+\-\d+))_(?P<date_to>(\d+\-\d+\-\d+))$', views.party_trial_detail, name='party_trial_detail'),
]