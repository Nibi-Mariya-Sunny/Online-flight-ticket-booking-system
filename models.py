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
    objects = None
    addflightnameid = models.ForeignKey(Addflightname, on_delete=models.CASCADE)
    orgin = models.ForeignKey(Orgin, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    dtime = models.CharField(max_length=30)
    htime = models.IntegerField()
    mtime = models.IntegerField()
    dday = models.CharField(max_length=3)
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
    status= models.IntegerField()
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
class Payment(models.Model):
    userid = models.CharField(max_length=30)
    fid = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    amt = models.IntegerField()
    status = models.IntegerField()
class Bclass(models.Model):
    key = models.CharField(max_length=6)
    a1 = models.IntegerField()
    b1 = models.IntegerField()
    c1 = models.IntegerField()
    d1 = models.IntegerField()
    e1 = models.IntegerField()
    f1 = models.IntegerField()
    a2 = models.IntegerField()
    b2 = models.IntegerField()
    c2 = models.IntegerField()
    d2 = models.IntegerField()
    e2 = models.IntegerField()
    f2 = models.IntegerField()
    a3 = models.IntegerField()
    b3 = models.IntegerField()
    c3 = models.IntegerField()
    d3 = models.IntegerField()
    e3 = models.IntegerField()
    f3 = models.IntegerField()
class Eclass(models.Model):
    key = models.CharField(max_length=6)
    a4 = models.IntegerField()
    b4 = models.IntegerField()
    c4 = models.IntegerField()
    d4 = models.IntegerField()
    e4 = models.IntegerField()
    f4 = models.IntegerField()
    a5 = models.IntegerField()
    b5 = models.IntegerField()
    c5 = models.IntegerField()
    d5 = models.IntegerField()
    e5 = models.IntegerField()
    f5 = models.IntegerField()
    a6 = models.IntegerField()
    b6 = models.IntegerField()
    c6 = models.IntegerField()
    d6 = models.IntegerField()
    e6 = models.IntegerField()
    f6 = models.IntegerField()
    a7 = models.IntegerField()
    b7 = models.IntegerField()
    c7 = models.IntegerField()
    d7 = models.IntegerField()
    e7 = models.IntegerField()
    f7 = models.IntegerField()
    a8 = models.IntegerField()
    b8 = models.IntegerField()
    c8 = models.IntegerField()
    d8 = models.IntegerField()
    e8 = models.IntegerField()
    f8 = models.IntegerField()
    a9 = models.IntegerField()
    b9 = models.IntegerField()
    c9 = models.IntegerField()
    d9 = models.IntegerField()
    e9 = models.IntegerField()
    f9 = models.IntegerField()
    a10= models.IntegerField()
    b10= models.IntegerField()
    c10= models.IntegerField()
    d10= models.IntegerField()
    e10= models.IntegerField()
    f10= models.IntegerField()