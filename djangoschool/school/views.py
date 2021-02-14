from django.shortcuts import render #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาษ

def HomePage(request): 
	# return HttpResponse('<h1>Hello World</h1>')
	return render(request, 'school/home.html')


def AboutPage(request):
	return render(request, 'school/about.html')

def ContactUs(request):
	return render(request, 'school/contact.html')
