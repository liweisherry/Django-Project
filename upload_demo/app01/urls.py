from django.contrib import admin
# from django import pat
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', views.Upload.as_view()),
    url(r'^index/', views.index),
    # url(r'^blog/[0-9]{4}/\d{2}/$',views.blogs),
    url(r'^blog/$',views.blog,name='blog'),
    #url(r'^blog/(?P<year>[0-9]{4})/(?P<month>\d{2})/$', views.blogs)
]
