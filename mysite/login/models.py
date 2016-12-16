from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    def __str__(self):
    	return self.username

class Data(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.CharField(max_length=200)

    def __str__(self):
    	return self.username.username + ": " + self.data


    
