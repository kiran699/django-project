from django.db import models


# Create your models here.
class  contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=50)
    birthdate=models.CharField(max_length=50)
    gendermale=models.CharField(max_length=50)
    genderfemale=models.CharField(max_length=50)
    gendernone=models.CharField(max_length=50)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    postalcode=models.CharField(max_length=50)

