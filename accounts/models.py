from django.db import models

# Create your models here.
class addMember(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    date=models.DateField()
    # REQUIRED_FIELD=['fname','lname','age','gender','username','password','image','date','date']

    def __str__(self):
        return self.fname


