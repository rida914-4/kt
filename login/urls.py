from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/invalid/$', views.invalid_login),

]