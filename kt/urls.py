"""kt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = [
    url(r'^', include('login.urls')),
    url(r'^', include('dashboard.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^', include('mis.urls')),
    url(r'^', include('purchase.urls')),


    # asset + purchase
    # url(r'^purchase/$', views.invoice, name='purchase'),
    # url(r'^purchase/(?P<voucher_id>\w+\d+)$', views.purchase, name='purchase'),
    # url(r'^main/', views.main_master_detail, name='main'),
    # url(r'^search/', views.search_master_detail, name='search'),
    # url(r'^new/', views.master_detail_new, name='new'),
    # url(r'^save/$', views.master_detail_save, name='save'),
    # url(r'^post/$', views.master_detail_post, name='post'),
    # url(r'^del/$', views.master_detail_del, name='del'),
    # url(r'^next/$', views.master_detail_next, name='next'),
    # url(r'^previous/$', views.master_detail_previous, name='previous'),
    # url(r'^first/$', views.master_detail_first, name='first'),
    # url(r'^last/$', views.master_detail_last, name='last'),
    #

    #

    #
    #
    #
    #
    #
    #
    #
    # url(r'sales', views.index, name='index'),
    # url(r'stock', views.index, name='index'),
    # url(r'utils', views.index, name='index'),
    # url(r'master', views.index, name='index'),
    # # url(r'form', views.Form, name='form'),
    # # url(r'purchase', views.purchase),
    # url(r'upload', views.copy_of_upload),
    # url(r'pdf', views.pdf_report),
    #
    #
    #
    #
    #
    #
    # # url(r'forms', views.get_form),
    # # url(r'^post/new/$', views.post_new, name='post_new'),
    # # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # #
    # url(r'create/$', views.create),
    # # url(r'detail/$', views.post_detail),
    # # url(r'list/$', views.post_list),
    # # url(r'update/$', views.post_update),
    # # url(r'delete/$', views.post_delete),
    # url(r'thanks', views.index),
    # url(r'thanks', views.index),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
