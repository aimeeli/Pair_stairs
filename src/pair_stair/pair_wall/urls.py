from django.conf.urls.defaults import patterns, include, url
from pair_stair.pair_wall.views import stairs_display, pairstairs_add_programmer, add_pair_count

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^addprogrammer/$', pairstairs_add_programmer),
    url(r'^pairstairs/$', stairs_display),
    url(r'^addcount/(?P<first_member>\w+)&(?P<second_member>\w+)/$', add_pair_count)
    # Examples:
    # url(r'^$', 'pair_stair.views.home', name='home'),
    # url(r'^pair_stair/', include('pair_stair.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
