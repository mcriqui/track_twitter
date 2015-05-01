from django.conf.urls import patterns, include, url
from django.contrib import admin
from tweet_stream import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.twitter_template, name='twitter_template'),
)
