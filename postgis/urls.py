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
    # This is "default" Db all table_schemas and table_name output
    url(r'^defaultdb/', views.defaultdb_view, name='defaultdb_name'),
    # This is "dbconn1" Db all table_schemas and table_name output
    url(r'^dbconn1/', views.dbconn1_view, name='dbconn1_name'),
    # This is "dbconn1" Db = a particular table and all containing data
    url(r'^(?P<tbl_name>\w+)/dbconn1/$', views.dbconn1_tbl_view, name='dbconn1_tbl_name'),
    # This is "dbconn1" Db = a particular table and particular gid
    # Regular expression for alphabets : \w+
    # Regular expression for numbers (integers) : \d+
    url(r'^(?P<tbl_name>\w+)/(?P<gid>\d+)/dbconn1/$', views.dbconn1_tbl_gid_view, name='dbconn1_tbl_gid_name'),
    # This is "dbconn1" Db = a particular table and route between two points using pgr_aStarFromAtoB()
    # Regular expression for decimal numbers : \d+\.\d*
    # More details on Regular expressions :
    # https://docs.python.org/2/howto/regex.html
    # https://docs.python.org/2/library/re.html#re-syntax
    # https://docs.python.org/2/library/re.html#re.DOTALL
    url(r'^(?P<tbl_name>\w+)/(?P<long_st>\d+\.\d*)/(?P<lat_st>\d+\.\d*)/(?P<long_end>\d+\.\d*)/(?P<lat_end>\d+\.\d*)/pgr_aStarFromAtoB/$', views.dbconn1_tbl_pts_pgr_aStarFromAtoB_view, name='dbconn1_tbl_pts_pgr_aStarFromAtoB_name'),

    # This is "dbconn1" Db post method
    url(r'^post/', views.post_test, name='post_test'),
    
)
