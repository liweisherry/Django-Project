"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(publisher|book|author)_del/(\d+)', views.delete,name='del'),
    url(r'^publisher_list/', views.publisher_list,name='publisher'),
    url(r'^publisher_add/', views.PublisherAdd.as_view(),name='pub_add'),
    # url(r'^publisher_del/', views.publisher_del),
    url(r'^publisher_edit/(\d+)', views.publisher_edit,name='pub_edit'),

    url(r'^book_list/', views.book_list, name = 'book'),
    # url(r'^book_del/', views.book_del),
    url(r'^book_add/', views.book_add),
    url(r'^book_edit/', views.book_edit),

    url(r'^author_list/', views.author_list, name = 'author'),
    url(r'^author_add/', views.author_add),
    # url(r'^author_del/', views.author_del),
    url(r'^author_edit/', views.author_edit),
]
