"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from ToDoList import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.all_list, name='index'),
    url(r'^$', views.todolist, name='todo'),
    url(r'^add/$', views.add_todo, name='add'),
    url(r'^success/(?P<id>\d+)/$', views.finish_reappear, name='success'),
    url(r'^failed/(?P<id>\d+)/$', views.finish_unreappear, name='failed'),
    url(r'^back/(?P<id>\d+)/$', views.todoback,  name='back'),
    url(r'^update/(?P<id>\d+)/$', views.update_todo, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.tododelete, name='delete'),
    url(r'^user/(?P<username>.*)/$', views.user_page, name='user'),
]
