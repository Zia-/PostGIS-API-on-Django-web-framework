from django.shortcuts import render
# For HttpResponse function
from django.http import HttpResponse
# For Db connections: connection is used for default Db and connections for other Dbs
from django.db import connection
from django.db import connections
# For simplejson output during return stage
import json as simplejson
import os
# To use templates created under the postgis/templates/postgis dir
	# we have created another postgis dir after templates coz Django
	# will search for all the templates inside the templates dir for all the apps
	# and then there could be soo many index.html for diff apps. 
	# Using the above approach we are referring to the 
	# index.html file like /postgis/index.html
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm

# Create your views here.

# View 1: Default welcome note.
def welcomenote_view(request):
    return HttpResponse("Welcome to National Innovation and Research Center for Geographical Information Technologies PostGIS Web-Server API Services!")

# View 2: "dbconn1" Db = a particular table and route between two points using pgr_aStarFromAtoB()
def pgr_aStarFromAtoB_view(request, username, tbl_name, long_st, lat_st, long_end, lat_end):
	cursor = connections[username].cursor()
	cursor.execute("SELECT name, cost, x1, y1, x2, y2 FROM pgr_aStarFromAtoB(%s, %s, %s, %s, %s) ORDER BY seq", [tbl_name, long_st, lat_st, long_end, lat_end])
	# Above approach should be used when there are too many arguments
	result = []
	fields = ['name', 'length', 'long_st', 'lat_st', 'long_end', 'lat_end']
	result.append(fields)
	for i in cursor:
		row = i
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 3: This is for the search functionality. It will take the text argument, been typed by by the user plus his/her current coord and will show the nearest 3 places with that text.
def search_view(request, username, tbl_name, clmn_name, search_txt, long_current, lat_current):
	cursor = connections[username].cursor()
	# The following approach is the best
	# "like" will be case sensitive, but "ilike" is not. So I am using "ilike"
	query = "select name, x, y from " + tbl_name + " where " + clmn_name + " ilike '%" + search_txt + "%' order by the_geom <-> ST_GeomFromText('POINT(" + long_current + "  " + lat_current + ")', 4326) LIMIT 3"
	cursor.execute(query)
	# The following appraoch is giving this kind of error: select name, x, y from 'ways_vertices_pgr' .... Syntex error
	#cursor.execute("select name, x, y from %s where id = 1"+
	#		"order by the_geom <-> ST_GeomFromText('POINT(%s %s)')"+ 		
	#		"LIMIT 3", [tbl_name, clmn_name, long_current, lat_current])	
	result = []
	fields = ['name', 'x', 'y']
	result.append(fields)
	for i in cursor:
		row = i
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 4: List all the exisitng tables inside a given Db along with its size (for the time being, there is only one Db for each user)
def db_view(request, username):
	cursor = connections[username].cursor()
	query = "select pg_database_size(current_database());"
	cursor.execute(query)
	for i in cursor:
		# Size is in bytes
		size = i[0]
	query = "SELECT * FROM information_schema.tables;"
	cursor.execute(query)
	result = []
	fields = [['table_catalog', 'table_schema', 'table_name', 'table_type', 'self_referencing_column_name', 'reference_generation', 'user_defined_type_catalog', 'user_defined_type_schema', 'user_defined_type_name', 'is_insertable_into', 'is_typed', 'commit_action'], 'db_size']
	result.append(fields)
	for i in cursor:
		#row = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], size]
		row = [i, size]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)
	
# View 5: List all the columns of a given "tbl_name"
def tbl_view(request, username, tbl_name):
	cursor = connections[username].cursor()
	query = "select count(*) from " + tbl_name + ""
	cursor.execute(query)
	for i in cursor:
		# Number of rows
		rows_count = i[0] 
	query = "select * from INFORMATION_SCHEMA.COLUMNS where table_name = '" + tbl_name + "';"
	cursor.execute(query)
	result = []
	fields = [['table_catalog', 'table_schema', 'table_name', 'column_name', 'ordinal_position', 'column_default', 'is_nullable', 'data_type', 'charaster_maximum_length', 'character_octet_length', 'numeric_precision', 'numeric_precision_radix', 'numeric_scale', 'datetime_precision', 'interval_type', 'interval_precision', 'character_set_catalog', 'character_set_schema', 'character_set_name', 'collation_catalog', 'collation_schema', 'collation_name', 'domain_catalog', 'domain_schema', 'domain_name', 'udt_catalog', 'udt_schema', 'udt_name', 'scope_catalog', 'scope_schema', 'scope_name', 'maximum_cardinality', 'dtd_identifier', 'is_self_referencing', 'is_identity', 'identity_generation', 'identity_start', 'identity_increment', 'identity_maximum', 'identity_minimum', 'identity_cycle', 'is_generated', 'generation_expression', 'is_updatable'], 'rows_count']
	result.append(fields)
	for i in cursor:
		row = [i, rows_count]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 6: Run a custom SQL query directly passed on by the user
def sql_view(request, username, sql_query):
	cursor = connections[username].cursor()
	# I think there is no need to drop this temp table as it will be auto dropped after this whole operation
	# I am not using this approach to decipher all other functions column names as I don't wanna perform 
	# this temp table creation operation and the query will be executed twice. Which I think is not good
	query = "create temp table " + username + " as " + sql_query + " limit 0"
	cursor.execute(query)
	query = "select column_name from INFORMATION_SCHEMA.COLUMNS where table_name = '" + username + "';"
	cursor.execute(query)
	clmn = []
	for i in cursor:
		clmn_name = i[0]
		clmn.append(clmn_name)
	query = sql_query
	cursor.execute(query)
	result = []
	result.append(clmn)
	for i in cursor:
		row = i
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 7: Create buffer taking all the arguments
def buffer_view(request, username, tbl_name, clmn_name, rad, seg):
	cursor = connections[username].cursor()
	query = "select st_asewkt(st_buffer(" + clmn_name + ", " + rad + ", 'quad_segs=" + seg + "')) from " + tbl_name + " where gid < 100"
	cursor.execute(query)
	result = []
	#result.append(clmn)
	for i in cursor:
		row = i
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)




































# View 2: Default alert message.
def alert_view(request):
	return HttpResponse("This is an alert message generated by ""postgis"" app")

# View 3: "default" Db all table_names and table_schemas
def defaultdb_view(request):
	cursor = connection.cursor()
	cursor.execute("SELECT table_schema,table_name "+
			"FROM information_schema.tables "+
			"ORDER BY table_schema,table_name;")
	result = []
	fields = ['table_schema', 'table_name']
	result.append(fields)
	for i in cursor:
		row = [i[0], i[1]]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 4: "dbconn1" Db all table_names and table_schemas
def dbconn1_view(request):
	cursor = connections['dbconn1'].cursor()
	cursor.execute("SELECT table_schema,table_name "+
			"FROM information_schema.tables "+
			"ORDER BY table_schema,table_name;")
	result = []
	fields = ['table_schema', 'table_name']
	result.append(fields)
	for i in cursor:
		row = [i[0], i[1]]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 5: "dbconn1" Db = a particular table and all containing data
# (1) Here I have converted "i[7]" to a string coz JSON notation has only a handful of native
# datatypes (objects, arrays, strings, numbers, booleans, and null), so anything serialized in
# JSON needs to be expressed as one of these types. i[7] is a numeric.
# (2) I can even add the "geom" column also and corresponding i[12] but it's just making
# request slow and its info is useless
def dbconn1_tbl_view(request, tbl_name):
	cursor = connections['dbconn1'].cursor()
	cursor.execute("SELECT * FROM %s" % tbl_name)
	result = []
	fields = ['gid', 'FIPS', 'ISO2', 'ISO3', 'UN', 'NAME', 'AREA', 'POP2005', 'REGION', 'SYBREGION', 'LON', 'LAT']
	result.append(fields)
	for i in cursor:
		row = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], str(i[7]), i[8], i[9], i[10], i[11]]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)

# View 6: "dbconn1" Db = a particular table and particular gid
def dbconn1_tbl_gid_view(request, tbl_name, gid):
	cursor = connections['dbconn1'].cursor()
	cursor.execute("SELECT * FROM %s where gid = %s" % (tbl_name, gid))
	# Another approach: cursor.execute("SELECT * FROM {0} where gid = {1}".format(tbl_name, gid))
	# But I think this is working only for 2 points
	result = []
	fields = ['gid', 'FIPS', 'ISO2', 'ISO3', 'UN', 'NAME', 'AREA', 'POP2005', 'REGION', 'SYBREGION', 'LON', 'LAT']
	result.append(fields)
	for i in cursor:
		row = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], str(i[7]), i[8], i[9], i[10], i[11]]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)	


# View 7: template test
def template_test(request):
	#latest_question_list = "ZIa"
	template = loader.get_template('postgis/index.html')
	#context = RequestContext(request, {"latest_question_list": latest_question_list})
	#return HttpResponse(template.render(context))
	context = RequestContext(request)
	return HttpResponse(template.render(context))
	
# View 8: Post feed Db
def post_test(request):
	if request.method == "POST":
		#form = ContactForm(request.POST)
		return HttpResponse(request.POST.get('id'))

# View 9: Post Upload file
def upload_test(request):
	template = loader.get_template('postgis/file_upload.html')
	#context = RequestContext(request, {"latest_question_list": latest_question_list})
	#return HttpResponse(template.render(context))
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def uploadresponse_test1(request):
	if request.method == "POST":
		#form = ContactForm(request.POST)
		osm = request.POST.get('myFile')
		os.system("osm2pgrouting -file %s -conf /usr/share/osm2pgrouting/mapconfig.xml -host localhost -port 5432 -dbname djangoapi2 -user postgres -passwd zia123 -prefixtables kn_ -clean" % (osm))
		return HttpResponse("uploadedddd")





def handle_uploaded_file(f):
    with open('/home/zia/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def uploadresponse_test(request):
    if request.method == 'POST':
        #form = UploadFileForm(request.POST, request.FILES)
	#if form.is_valid():
	f = request.FILES['fileosm']
	with open('/home/zia/Documents/Codes/Django/sql_api/downloads_users/name.osm', 'wb+') as destination:
        	for chunk in f.chunks():
            		destination.write(chunk)
	os.system("ls > someFile.txt")	
	os.system("osm2pgrouting -file /home/zia/Documents/Codes/Django/sql_api/downloads_users/name.osm -conf /usr/share/osm2pgrouting/mapconfig.xml -host localhost -port 5432 -dbname djangoapi2 -user postgres -passwd zia123 -prefixtables kn5_ -clean")
        return HttpResponse("true1")
    else:
        return HttpResponse('false')
    #return HttpResponse("assss")

