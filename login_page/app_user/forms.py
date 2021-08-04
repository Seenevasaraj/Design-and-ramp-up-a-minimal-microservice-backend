from django import forms
from django.contrib.auth.models import User
from app_user.models import user_profile
from django.contrib.auth.forms import UserCreationForm
	

class Userform(UserCreationForm):
	email=forms.EmailField()

	class Meta():
		model=User
		fields=('username','first_name','last_name','email','password1','password2')
		labels={
		'password1','Password'
		'password2','Conform Password'
		}
class UserProfileInfoform(forms.ModelForm):
	bio=forms.CharField(required=False)

	class Meta():
		 model=user_profile
		 fields=('bio','img')
			
						

	