"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from article import urls as article_urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/',include(article_urls)),
    url(r'^accounts/login/$','django_test.views.login'),
    url(r'^accounts/auth/$','django_test.views.auth_view'),
    url(r'^accounts/logout/$','django_test.views.logout'),
    url(r'^accounts/loggedin/$','django_test.views.loggedin'),
    url(r'^accounts/invalid/$','django_test.views.invalid_login'),
    url(r'^accounts/register/$','django_test.views.register_user'),
    url(r'^accounts/register_success/$','django_test.views.register_success'),


]
