from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.db import connection
from django.db import connections

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.Zia this is.")

def alertmsg(request):
	return HttpResponse("This is one custom alert by Zaaa!")

#@api_view(['GET', 'POST'])
def msg(request):
	if request.method == 'GET':
		return HttpResponse("get1")
	# POST method cant be of return type	
	#elif request.method == 'POST':
	#	return HttpResponse("post1")

def detail(request, question_id):
	return HttpResponse("Your looking at question %s" % question_id)

def results(request, question_id):
	response = "Yore looking at results of quesiton %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Your voting on question %s" % question_id)

def new(request, newarg1, newarg2):
	return HttpResponse("New Args are = %s %s" % (newarg1, newarg2))

def dbget1(request):
	cursor = connection.cursor()
	# for other Db connections : cursor = connections['db2'],cursor()
	cursor.execute("select * from world where gid = 1")
	row = cursor.fetchone()
	#return row
	return HttpResponse("New11")

	#desc = cursor.description
    	#return [
        #dict(zip([col[0] for col in desc], row))
        #for row in cursor.fetchall()
    	#]



