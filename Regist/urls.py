from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^search$', views.search, name='search'),
    url(r'^push$', views.push, name='push'),
    url(r'^searchPush$', views.searchPush, name='searchPush'),
    url(r'^confirmPush$', views.confirmPush, name='confirmPush'),
]