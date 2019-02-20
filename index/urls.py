"""index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
from . import views
import game.views

urlpatterns = [
    url(r'^$',views.main, name='main'),
    url(r'^login/$',views.login, name='login'),
    url(r'^mainpage/$', game.views.index, name='index'),
    #url(r'^mainpage/$',)
    url(r'^accounts/', include('allauth.urls')),
    url(r'^do', game.views.do, name='do'),
    url(r'^admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
