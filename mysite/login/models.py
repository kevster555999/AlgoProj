from django.db import models

# Create your models here.
class loginScreen(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__():
    		print "UserName: ",username," Password: ",password