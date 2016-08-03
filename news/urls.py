from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from news import views
from django.core.urlresolvers import reverse

urlpatterns = [
	url(r'^$', views.news_main),
    url(r'^(?P<news_id>\w+)/(?P<slug>.+)$', views.news_page)
]