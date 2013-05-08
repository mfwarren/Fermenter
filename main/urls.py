from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
        url(r'^$', 'dashboard', name='dashboard'),
        url(r'^start-brew/$', 'start_brew', name='start-brew'),
        url(r'^finish-brew/$', 'finish_brew', name='finish-brew'),
        )
