from django.db import models

# Create your models here.
class IdCount(models.Model):
    id = models.IntegerField(primary_key=True)


class Proposer(models.Model):
    app_id =  models.IntegerField()
    password = models.CharField(max_length = 256)
    name = models.CharField(max_length = 63)
    email = models.EmailField(unique = True)
    mob = models.CharField(max_length = 63)
    alumini = models.BooleanField(default = False)
    staff = models.BooleanField(default = False)
    something = models.BooleanField(default = False)
    yop = models.CharField(max_length = 63)
    degree = models.CharField(max_length = 63)
    dept = models.CharField(max_length = 63)
    specialization = models.CharField(max_length = 63)
    award =  models.CharField(max_length = 63)
    address = models.CharField(max_length = 255)
    submitted = models.BooleanField(default = False)
    
    
class ALAA_Form(models.Model):
    name_proposer = models.CharField(max_length = 200)
    details_proposer = models.TextField(blank = False)
    proposer_address = models.TextField(blank = False)
    proposer_mob = models.CharField(max_length = 16)
    proposer_email = models.CharField(max_length=63)
    name_nominee = models.CharField(max_length=63)
    nominee_father_name = models.CharField(max_length=63)
    dob = models.CharField(max_length=63)
    degree = models.CharField(max_length=63)
    dept = models.CharField(max_length=63)
    yop = models.CharField(max_length=63)
    rollno = models.CharField(max_length=63)
    otherquali = models.CharField(max_length=255)
    ppo = models.CharField(max_length=255)
    nominee_address = models.CharField(max_length=255)
    nominee_mob = models.CharField(max_length=16)
    nomionee_email = models.CharField(max_length=63)
    profile_pic = models.FileField(upload_to='documents/%Y/%m/%d')
    accom = models.FileField(upload_to='documents/%Y/%m/%d')