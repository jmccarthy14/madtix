from django.conf.urls import patterns, url
from api.views import TicketsView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tix.views.home', name='home'),
    # url(r'^tix/', include('tix.foo.urls')),
    url(r'^$', 'api.views.index', name='index'),
    url(r'^tickets$', TicketsView.as_view(), name='tickets'),
    url(r'^create_ticket$', 'api.views.create_ticket', name='create_ticket')
)