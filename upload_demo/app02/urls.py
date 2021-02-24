from django.contrib import admin
# from django import pat
from django.conf.urls import url
from app02 import views

urlpatterns = [

    url(r'^article/', views.article),
    # url(r'^blog/[0-9]{4}/\d{2}/$',views.blogs),
    url(r'^article/(?P<year>[0-9]{4})/(?P<month>\d{2})/$', views.articles)
]
