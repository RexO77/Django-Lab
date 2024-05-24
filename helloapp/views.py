from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	print('inside Hello')
	retutn HttpResponse('<h1>Hey There</h1>')