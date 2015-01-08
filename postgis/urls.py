# This urls.py was created manually
from django.conf.urls import patterns, url

from postgis import views

urlpatterns = patterns('',
    # ex: localhost:8000/postgis/
    # This will run the function named "index" coz of "views.index" in the "views.py" file
    # The use of "name='index'" is not clear
    url(r'^$', views.index_view, name='index_name'),
    # This is just an alert message
    url(r'^alert/', views.alert_view, name='alert_name'),
    # This is default Db sample output
    url(r'^defaultdb/', views.defaultdb_view, name='defaultdb_name'),
    # This is dbconn1 Db sample output
    url(r'^dbconn1/', views.dbconn1_view, name='dbconn1_name'),
)
