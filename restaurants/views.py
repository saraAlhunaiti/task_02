from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
	context ={
		"msg":"Hello Wrld"
	}
	
	return render(request, 'hello.html', context)