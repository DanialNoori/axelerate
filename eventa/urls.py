from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from eventa import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^', views.events_page, name='post_page')
]