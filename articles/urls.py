from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from articles import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^(?P<post_id>\w+)/(?P<slug>.+)/$', views.post_page, name='post_page')
]