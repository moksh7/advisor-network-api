from django.db import models
from django.conf import settings

# Create your models here.
class Advisor(models.Model):
    name = models.CharField(max_length=40,unique=True)
    photo = models.ImageField(upload_to='images/')

class Booking(models.Model):
    '''Model to store data about every appointment'''
    
    appointment = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE)