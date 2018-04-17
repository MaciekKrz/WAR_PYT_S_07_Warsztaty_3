"""warsztat_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from exercises.views import (start_page, room, new_room, modify_room, delete_room, search_room, reserve_room
                              )

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^start_page/$', start_page),
    url(r'^room/(?P<my_id>(\d)+)/$', room),
    url(r'^room/new/$', new_room),
    url(r'^room/modify/(?P<my_id>(\d)+)/$', modify_room),
    url(r'^room/delete/(?P<my_id>(\d)+)/$', delete_room),
    url(r'^room/search/$', search_room),
    url(r'^room/reservation/(?P<my_id>(\d)+)/$', reserve_room),
]
