# This urls.py was created manually
from django.conf.urls import patterns, url

from postgis import views

urlpatterns = patterns('',
    # ex: localhost:8000/postgis/
    # This will run the function named "index" coz of "views.index" in the "views.py" file
    # The use of "name='index'" is not clear
    url(r'^$', views.welcomenote_view, name='welcomenote_name'),
    # This is "dbconn1" Db = a particular table and route between two points using pgr_aStarFromAtoB()
    # Regular expression for decimal numbers : \d+\.\d*
    # More details on Regular expressions :
    # https://docs.python.org/2/howto/regex.html
    # https://docs.python.org/2/library/re.html#re-syntax
    # https://docs.python.org/2/library/re.html#re.DOTALL
    url(r'^(?P<username>\w+)/(?P<tbl_name>\w+)/pgr_aStarFromAtoB/(?P<long_st>\d+\.\d*)/(?P<lat_st>\d+\.\d*)/(?P<long_end>\d+\.\d*)/(?P<lat_end>\d+\.\d*)/$', views.pgr_aStarFromAtoB_view, name='pgr_aStarFromAtoB_name'),
    # This is for the search functionality. It will take the text argument, been typed by
    # by the user plus his/her current coord and will show the nearest 3 places with that text.
    url(r'^(?P<username>\w+)/(?P<tbl_name>\w+)/(?P<clmn_name>\w+)/(?P<search_txt>\w+)/(?P<long_current>\d+\.\d*)/(?P<lat_current>\d+\.\d*)/$', views.search_view, name='search_name'),
    # This will give the existing tables info about the provided db name 
    url(r'^(?P<username>\w+)/db//$', views.db_view, name='db_name'),
    # This will give the column info a the provided table name 
    url(r'^(?P<username>\w+)/db//tbl/(?P<tbl_name>\w+)/$', views.tbl_view, name='tbl_name'),












    











    
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
    
    # This is "dbconn1" Db template
    url(r'^template/$', views.template_test, name='template_test'),
    # This is "dbconn1" Db post
    url(r'^post/$', views.post_test, name='post_test'),
    # This is "dbconn1" Db upload file
    url(r'^upload/$', views.upload_test, name='upload_test'),
    # This is "dbconn1" Db upload file
    url(r'^uploadresponse/$', views.uploadresponse_test, name='uploadresponse_test'),
    
)
