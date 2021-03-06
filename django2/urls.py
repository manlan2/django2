"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from hello import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^hello/', views.hello, name='hello' ),
    url(r'^hello/', views.hello ),
    url(r'^hi/',    views.hi),
    url(r'^reg/',    views.register),
    url(r'^i/',    views.index),
    url(r'^index/',    views.index),
    url(r'^baidu/',    views.baidu),
    # url(r'^index/',    views.index ),
]
