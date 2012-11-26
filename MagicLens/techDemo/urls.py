from django.conf.urls import patterns, include, url

urlpatterns = patterns('techDemo.views',
    url(r'^magnifyingGlass/$', 'magnifyingGlass'),
    url(r'^screenDim/$', 'screenDim'),
    url(r'^resizeContent/$', 'resizeContent'),
    url(r'^textAnnotation/$', 'textAnnotation'),
    url(r'^viewCode/$', 'viewCode'),  
    url(r'^screenShot/$', 'screenShot'),   
    url(r'^textHighlight/$', 'textHighlight'), 
    url(r'^dummyWebsite/$', 'dummyWebsite'),
)
