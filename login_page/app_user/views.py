from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app_user.forms import Userform,UserProfileInfoform
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request,'home.html')



def register(request):
	registered=False
	if request.method=='POST':
		user_form=Userform(data=request.POST)
		profil_form=UserProfileInfoform(data=request.POST)

		if user_form.is_valid and profil_form.is_valid:
			user=user_form.save()
			user.save()

			profile=profil_form.save(commit=False)
			profile.user=user
			profile.save()
			registered=True
		else:
		    print(user_form.errors,profil_form.errors)

	else:
		user_form=Userform()
		profil_form=UserProfileInfoform()

	return render(request,'app_user/register.html',
		{'registered':registered,
		'user_form':user_form,
		'profil_form':profil_form
		})																				
 

def user_login(request):
    if request.method == 'POST':
      	username=request.POST.get('username')
      	password=request.POST.get('password')
      	user=authenticate(username=username,password=password)

      	if user:
      		if user.is_active:
      			login(request,user)
      			return HttpResponseRedirect(reverse('index'))
      		else:
      			print("USER IS OFFLINE")
      	else:
      		print("PLEASE ENTER CORRECT ID & PASSWORD")
    else:
    	return render(request,'app_user/login.html')
		
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

