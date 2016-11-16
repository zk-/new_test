from django.conf.urls import patterns, include, url

from django.contrib import admin
import test
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', test.index),
    url(r'^blog/', include('blog.urls')),
    url(r'^blogmanager/', include('blogmanager.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
