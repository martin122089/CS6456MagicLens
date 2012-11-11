from django.conf.urls import patterns, include, url

urlpatterns = patterns('techDemo.views',
    url(r'^magnifyingGlass/$', 'magnifyingGlass'),
    url(r'^screenDarkening/$', 'screenDarkening'),
    url(r'^screenDimExample/$', 'screenDimExample'),
)
