from django.db import models

# Create your models here.
class Location(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    def __str__(self):
        return self.title
        


class Image(models.Model):
    image=models.ImageField(upload_to='images')
    name=models.CharField(max_length=200)
    address=models.TextField()
    Desc=models.CharField(max_length=200,null=True)
    mob=models.CharField(max_length=200,null=True)
    need=models.CharField(max_length=200,null=True)
    map=models.URLField(max_length=200,null=True)
    added_date=models.DateTimeField(auto_now_add=True)
    loc=models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Upload(models.Model):
    photo =models.ImageField(upload_to="media")
    name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)

