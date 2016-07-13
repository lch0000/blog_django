from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.get_blogs', name='blog_get_blogs'),
    url(r'^detail/(\d+)/$', 'blog.views.get_detail', name='blog_get_detail'),
)
