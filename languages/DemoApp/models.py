from django.db import models

# Create your models here.
class Reg(models.Model):
    name=models.CharField(max_length=20)
    passc=models.CharField(max_length=15)
    cont=models.CharField(max_length=20)
    ad=models.CharField(max_length=50,primary_key=True)

class Savefile(models.Model):
    user = models.CharField(max_length=50)
    ids=models.IntegerField()
    paragraphs = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    srclang=models.CharField(max_length=40)
    destlang=models.CharField(max_length=40)
    srctext=models.CharField(max_length=5000)
    desttext=models.CharField(max_length=5000)