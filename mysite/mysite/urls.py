"""mysite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from mysite.views import dev, platformsh, current_datetime, hours_ahead, display_meta, contact, users_list, view_1, view_2
from django.contrib.auth.views import login, logout
from mysite.books import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/$', current_datetime, name='current_time'),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead, name='ahead_time'),
    url(r'^meta/$', display_meta),
    url(r'^contact',contact),
    # url(r'^v1/$',view_1),
    # url(r'^v2/$',view_2),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^authors/$', views.author_list),
    # url(r'^account/login/$', login),
    # url(r'^account/logout/$', logout),
    url(r'^users$', users_list),
    url(r'^',platformsh),
]

