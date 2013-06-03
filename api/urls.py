from django.conf.urls import patterns, url
from api.views import TicketsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^base/', include('foo.urls')),
    url(r'^$', 'api.views.index', name='index'),
    url(r'^tickets$', TicketsView.as_view(), name='tickets')
)