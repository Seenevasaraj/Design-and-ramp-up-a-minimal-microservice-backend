from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
def path_and_rename(instance,filname):
		upload_to='Images/'
		ext=filname.spilit('.')[-1]
		if instance.user.username:
			filname='user_Profile_Pictures/{}.{}'.format(instance.user.username,ext)		
		return os.path.join(upload_to, filname)
												    
class user_profile(models.Model):
		user=models.OneToOneField(User,on_delete=models.CASCADE)
		bio=models.CharField(max_length=150,blank=True)
		img=models.ImageField(upload_to='path_and_rename',verbose_name='Profile picture',blank=True)


		def __str__(self):
			return(self.user.username)

		