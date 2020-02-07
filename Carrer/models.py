from django.db import models


class Carrer(models.Model):
    image= models.ImageField(upload_to='images/')
    whatyouhavedone = models.CharField(max_length=200)
    summary= models.CharField(max_length=200)
    Certification= models.BooleanField(default=False)