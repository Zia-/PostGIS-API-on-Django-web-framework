from django.conf.urls import patterns, url

from app1 import views

urlpatterns = patterns('',
    # ex: /app1/
    url(r'^$', views.index, name='index'),
    # ex: /app1/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /app1/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /app1/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    # ex: /app1/5/4/new/
    url(r'^(?P<newarg1>\d+)/(?P<newarg2>\d+)/new/$', views.new, name='new'),
    #
    url(r'^alert1/', views.alertmsg, name='allt'),
    url(r'^msg1/', views.msg, name='mss'),
)
