from django.db import models

# Create your models here.

class User_Cred_Roles(models.Model):
	# Details at https://docs.djangoproject.com/en/1.7/ref/models/fields/#emailfield
	id_user = models.AutoField(primary_key=True)
	session_key = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=75)
	password = models.CharField(max_length=100)
	pgr_astarfromatob = models.BooleanField(default=False) 

