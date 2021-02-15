from django.shortcuts import render, redirect #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาษ
from .models import ExamScore
from django.contrib.auth.models import User

def HomePage(request): 
	# return HttpResponse('<h1>Hello World</h1>')
	return render(request, 'school/home.html')


def AboutPage(request):
	return render(request, 'school/about.html')

def ContactUs(request):
	return render(request, 'school/contact.html')

def ShowScore(request):
	score = ExamScore.objects.all()			#ดึงค่ามาจากDBทั้งหมด

	context = {'score':score}

	return render(request, 'school/showscore.html', context)

def Register(request):

	if request.method == 'POST':
		data = request.POST.copy()
		first_name = data.get('first_name')					#Get data from html register
		last_name = data.get('last_name')
		email = data.get('email')
		password = data.get('password')

		newuser = User()
		newuser.username = email
		newuser.first_name = first_name
		newuser.last_name = last_name
		newuser.email = email
		newuser.set_password(password)			
		newuser.save()
		
		return redirect('home-page')

	return render(request, 'school/register.html')







