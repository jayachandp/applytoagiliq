from django.conf.urls import patterns, include, url

urlpatterns = patterns('uploadresume.views',
    
    url(r'^$', 'index', name='index'),
    url(r'^upload_resume$', 'upload_resume', name='upload_resume'),
    
)