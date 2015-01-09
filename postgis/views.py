from django.shortcuts import render
# For HttpResponse function
from django.http import HttpResponse
# For Db connections: connection is used for default Db and connections for other Dbs
from django.db import connection
from django.db import connections
# For simplejson output during return stage
import json as simplejson

# Create your views here.

# View 1: Default welcome note.
def index_view(request):
    return HttpResponse("Welcome to National Innovation and Research Center for Geographical Information Technologies PostGIS Web-Server API Services!")

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
# JSON needs to be expressed as one of these types.
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

# View 7: "dbconn1" Db = a particular table and route between two points using pgr_aStarFromAtoB()
def dbconn1_tbl_pts_pgr_aStarFromAtoB_view(request, tbl_name, long_st, lat_st, long_end, lat_end):
	cursor = connections['dbconn1'].cursor()
	cursor.execute("with x as ( "+
			"SELECT name, cost, geom FROM pgr_aStarFromAtoB(%s, %s, %s, %s, %s) ORDER BY seq) "+
			"select x.name as name, x.cost as length, st_x(st_startpoint(x.geom)) as long_st, "+ 
			"st_y(st_startpoint(x.geom)) as lat_st, st_x(st_endpoint(x.geom)) as long_end, st_y(st_endpoint(x.geom)) as lat_end "+ 
			"from x", [tbl_name, long_st, lat_st, long_end, lat_end])
	# Above approach should be used where there are too many arguments
	result = []
	fields = ['name', 'length', 'long_st', 'lat_st', 'long_end', 'lat_end']
	result.append(fields)
	for i in cursor:
		row = [i[0], i[1], i[2], i[3], i[4], i[5]]
		result.append(row)
	json_result = simplejson.dumps(result)
	return HttpResponse(json_result)









