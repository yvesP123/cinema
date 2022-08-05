from unicodedata import category
from django.db import models
# Create your models here.
class addMovie(models.Model):
    title=models.CharField(max_length=100)
    actor=models.CharField(max_length=100)
    poster=models.CharField(max_length=100)
    trailer=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    realedate=models.DateField()
    description=models.CharField(max_length=500)
    category=models.CharField(max_length=100)
    user_post=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(models.Value==1)
   
    # REQUIRED_FIELD=['fname','lname','age','gender','username','password','image','date','date']

    def __str__(self):
        return self.title


