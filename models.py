from django.db import models
class Register(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    phno = models.IntegerField()
    email = models.CharField(max_length=30)
class Login(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.IntegerField()
class Addflightname(models.Model):
    fname = models.CharField(max_length=30)
    eseats = models.IntegerField(max_length=30)
    bseats = models.IntegerField(max_length=30)
    ewseats = models.IntegerField(max_length=30)
    bwseats = models.IntegerField(max_length=30)
    motherchild = models.IntegerField(max_length=30)
    rseats = models.IntegerField(max_length=30)
class Addplace(models.Model):
    orgin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
class District(models.Model):
    name = models.CharField(max_length=30)

class Addflightschedule(models.Model):
    addflightnameid = models.ForeignKey(Addflightname, on_delete=models.CASCADE)
    addplaceid = models.ForeignKey(Addplace, on_delete=models.CASCADE)
    fname = models.CharField(max_length=30)
    orgin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    ddate = models.CharField(max_length=30,)
    dtime = models.CharField(max_length=30)
    adate = models.CharField(max_length=30)
    atime = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)

class Flightrate(models.Model):
    addflightscheduleid = models.ForeignKey(Addflightschedule, on_delete=models.CASCADE)
    amount = models.CharField(max_length=30)
class Addaddon(models.Model):
    aname = models.CharField(max_length=30)
    amount=models.IntegerField(max_length=30)
class Addpackage(models.Model):
    photo = models.FileField()
    pname = models.CharField(max_length=30)
    pamount=models.IntegerField(max_length=30)
