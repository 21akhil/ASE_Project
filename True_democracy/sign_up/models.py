from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	#Additional
	Aadhar_id = models.CharField('AADHAR',max_length=12,unique = True,blank = False)
	PhNo1 = models.CharField('PhNo1',max_length=10,blank = False)
	PhNo2 = models.CharField('PhNo2',max_length=10,blank = False)
	Name = models.CharField('Name',max_length=150,blank=False)
	def __str__(self):
		return self.Aadhar_id

