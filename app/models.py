from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photo/")
    
    def __str__(self):
        return self.username.username
    
class Budget(models.Model):
    slno = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    money = models.IntegerField()
    
    def __str__(self):
        return self.title