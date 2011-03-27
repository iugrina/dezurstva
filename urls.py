from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^dez/$', 'statistika.views.index'),
	(r'^dez/polls/(?P<poll_id>\d+)/$', 'statistika.views.detail'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^dez/admin/', include(admin.site.urls)),
)
