from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.Zia this is.")

def alertmsg(request):
	return HttpResponse("This is one custom alert by Zaaa!")
