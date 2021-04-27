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
    eseats = models.IntegerField()
    bseats = models.IntegerField()
    ewseats = models.IntegerField()
    bwseats = models.IntegerField()
    motherchild = models.IntegerField()
    rseats = models.IntegerField()
class Orgin(models.Model):
    orgin = models.CharField(max_length=30)

class Destination(models.Model):
    destination = models.CharField(max_length=30)
class District(models.Model):
    name = models.CharField(max_length=30)

class Addflightschedule(models.Model):
    addflightnameid = models.ForeignKey(Addflightname, on_delete=models.CASCADE)
    orgin = models.ForeignKey(Orgin, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    ddate = models.CharField(max_length=30,)
    dtime = models.CharField(max_length=30)
    adate = models.CharField(max_length=30)
    atime = models.CharField(max_length=30)
    amount = models.IntegerField()
    camount = models.IntegerField()
    iamount = models.IntegerField()
    wsamount = models.IntegerField()
    bcamount = models.IntegerField()
    weight = models.IntegerField()
class Booking(models.Model):
    addflightscheduleid = models.ForeignKey(Addflightschedule, on_delete=models.CASCADE)
    userid=models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phno = models.IntegerField()
    email = models.CharField(max_length=30)
class Flightrate(models.Model):
    addflightscheduleid = models.ForeignKey(Addflightschedule, on_delete=models.CASCADE)
    amount = models.CharField(max_length=30)
class Addaddon(models.Model):
    aname = models.CharField(max_length=30)
    amount=models.IntegerField()
class Addpackage(models.Model):
    photo = models.FileField()
    pname = models.CharField(max_length=30)
    pamount=models.IntegerField()
