from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tix.views.home', name='home'),
    # url(r'^tix/', include('tix.foo.urls')),
    url(r'^$', 'api.views.index', name='index')
)