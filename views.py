from django.shortcuts import render
from django . http import HttpResponse
from datetime import date, datetime
from requests_html import HTMLSession
import certifi
import lxml.html
import urllib.request
from.models import Register,Login,Addflightname,Orgin,Destination,District,Flightrate,Addflightschedule,Addaddon,Addpackage,Booking,Payment
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
  try:
    m=Login.objects.get(email=request.POST['email'],password=request.POST['password'])
    if m.status == 1:
        request.session['user']=m.email
        return render(request,'Userhome.html')
    elif m.status == 0:
        return render(request,'adminhome.html')
    else:
        return render(request,'login.html',{'error':"didn't match"})
  except:
     return render(request,'login.html',{'error':"Invalid Username or Password"})

def register(request):
    return render(request,'register.html')
def reg(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phno= request.POST['phno']
    email = request.POST['email']
    password = request.POST['password']
    data=Register(fname=fname,lname=lname,gender=gender,dob=dob,phno=phno,email=email)
    data.save()
    data1=Login(email=email,password=password,status=1)
    data1.save()
    return render(request, 'login.html')
def Userhome(request):
    user=request.session['user']
    data=Login.objects.filter(email=user)
    return render(request,'Userhome.html',{'data':data})
def adminhome(request):
    return render(request,'adminhome.html')
def report(request):
    return render(request,'report.html')
def addflightname(request):
    return render(request,'addflightname.html')
def addfname(request):
    '''import pdb;pdb.set_trace();'''
    fname = request.POST['fname']
    eseats = request.POST['eseats']
    bseats = request.POST['bseats']
    ewseats= request.POST['ewseats']
    bwseats = request.POST['bwseats']
    motherchild = request.POST['motherchild']
    rseats =int(motherchild)+int(bwseats)+int(ewseats)+int(bseats)+int(eseats)
    data = Addflightname(fname=fname, eseats=eseats, bseats=bseats,ewseats=ewseats,bwseats=bwseats,motherchild=motherchild,rseats=rseats)
    data.save()
    return render(request,'addflightname.html')
def addflightschedule(request):
    data = Addflightname.objects.all()
    data1 = Orgin.objects.all()
    data2=Destination.objects.all()
    return render(request,'addflightschedule.html',{'data':data,'d':data2,'o':data1})
'''def aaddfschedule(request):
    return render(request, 'addflightschedule.html')'''
def addfschedule(request):
    addflightnameid= request.POST['id']
    instance =Addflightname.objects.get(id=addflightnameid)

    org= request.POST['orgin']
    des = request.POST['destination']
    orgin = Orgin.objects.get(id= org)
    destination = Destination.objects.get(id=des)
    dtime = request.POST['dtime']
    htime=request.POST['htime']
    mtime=request.POST['mtime']
    amount = request.POST['amount']
    mon = request.POST.get('mon')
    tue = request.POST.get('tue')
    wed = request.POST.get('wed')
    thu = request.POST.get('thu')
    fri = request.POST.get('fri')
    sat = request.POST.get('sat')
    sun = request.POST.get('sun')
    camount =int(amount)-300
    iamount =int(amount)-500
    wsamount =int(amount)+500
    bcamount =int(amount)+2000
    weight = request.POST['weight']

    if mon == '0':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime,mtime=mtime,amount=amount,camount=camount,iamount=iamount, wsamount=wsamount,bcamount=bcamount,weight=weight,dday="Mon")
        data.save()
    if tue == '1':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                             wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Tue")
        data.save()
    if wed == '2':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                             wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Wed")
        data.save()
    if thu == '3':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                             wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Thu")
        data.save()
    if fri == '4':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                             wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Fri")
        data.save()
    if sat == '5':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                             wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Sat")
        data.save()
    if sun == '6':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                             htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                             wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Sun")
        data.save()

    return render(request,'addflightschedule.html')

def addflightrate(request):
    data=Addflightschedule.objects.all()
    return render(request,'addflightrate.html',{'data':data})
def addfrate(request):
    addflightscheduleid =request.POST['id']
    instance=Addflightschedule.objects.get(id=addflightscheduleid)
    amount = request.POST['amount']
    data = Flightrate(addflightscheduleid=instance,amount=amount)
    data.save()
    return render(request,'addflightrate.html')
def addplace(request):
    return render(request,'addplace.html')
def placereg(request):
    orgin = request.POST['orgin']
    destination = request.POST['destination']
    data =Orgin(orgin=orgin)
    data.save()
    data =Destination(destination=destination)
    data.save()
    return render(request,'addplace.html')
def adddistrict(request):
    data = State.objects.all()
    return render(request,'adddistrict.html',{'d':data})
def districtreg(request):
    name = request.POST['name']
    data = District(name=name)
    data.save()
    return render(request,'adddistrict.html')
def addaddon(request):
    return render(request,'addaddon.html')
def addonreg(request):
    aname = request.POST['aname']
    amound = request.POST['amound']
    data = Addaddon(aname=aname,amount=amound)
    data.save()
    return render(request,'addaddon.html')
def addpackage(request):
    return render(request,'addpackage.html')
def packagereg(request):
    photo=request.FILES['file']
    pname = request.POST['pname']
    pamount = request.POST['pamount']
    data = Addpackage(photo=photo,pname=pname, pamount=pamount)
    data.save()
    return render(request,'addpackage.html')
def showflightname(request):
    data = Addflightname.objects.all()
    return render(request,'showflightname.html',{'data':data})
def showflightschedule(request):
    data = Addflightschedule.objects.all()
    return render(request,'showflightschedule.html',{'d':data})
def showflightrate(request):
    data = Flightrate.objects.all()
    return render(request,'showflightrate.html',{'d':data})
def showplaces(request):
    data = Orgin.objects.all()
    data1 = Destination.objects.all()
    return render(request,'showplaces.html',{'d':data,'data1':data1})
def showdistrict(request):
    data = District.objects.all()
    return render(request,'showdistrict.html',{'d':data})
def showaddon(request):
    data = Addaddon.objects.all()
    return render(request,'showaddon.html',{'d':data})
def showpackage(request):
    data = Addpackage.objects.all()
    return render(request,'showpackage.html',{'d':data})
def editflightname(request):
    id=request.POST['id']
    data=Addflightname.objects.get(id=id)
    return render(request,'editflightname.html',{'data':data})
def showregisteredusers(request):
    data = Register.objects.all()
    return render(request,'showregisteredusers.html',{'data':data})

def myprofile(request):
    email = request.session['user']
    data = Register.objects.filter(email=email)
    return render(request,'myprofile.html',{'data':data})
def update(request):
    id=request.POST['id']
    data=Addflightname.objects.get(id=id)
    data.fname=request.POST['fname']
    data.eseats = request.POST['eseats']
    data.bseats = request.POST['bseats']
    data.ewseats = request.POST['ewseats']
    data.bwseats = request.POST['bwseats']
    data.motherchild = request.POST['motherchild']
    data.rseats = request.POST['rseats']
    data.save()
    data = Addflightname.objects.all()
    return render(request, 'showflightname.html', {'data': data})
def editflightschedule(request):
    id = request.POST['i.id']
    data = Addflightschedule.objects.get(id=id)
    return render(request, 'editflightschedule.html', {'data': data})
def updateflightschedule(request):
    id=request.POST['id']
    i=Addflightschedule.objects.get(id=id)
    i.fname = request.POST['fname']
    i.orgin.orgin = request.POST['orgin']
    i.destination.destination = request.POST['destination']
    i.dday = request.POST['dday']
    i.dtime = request.POST['dtime']
    i.htime = request.POST['htime']
    i.mtime = request.POST['mtime']
    i.amount = request.POST['amount']
    i.mon = request.POST['mon']
    i.tue = request.POST['tue']
    i.wed = request.POST['wed']
    i.thu = request.POST['thu']
    i.fri = request.POST['fri']
    i.sat = request.POST['sat']
    i.sun = request.POST['sun']
    weight = request.POST['weight']

    if mon == '0':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Mon")
        data.save()
    if tue == '1':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Tue")
        data.save()
    if wed == '2':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Wed")
        data.save()
    if thu == '3':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Thu")
        data.save()
    if fri == '4':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Fri")
        data.save()
    if sat == '5':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Sat")
        data.save()
    if sun == '6':
        data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, dtime=dtime,
                                 htime=htime, mtime=mtime, amount=amount, camount=camount, iamount=iamount,
                                 wsamount=wsamount, bcamount=bcamount, weight=weight, dday="Sun")
        data.save()


    data = Addflightschedule.objects.all()
    return render(request, 'showflightschedule.html', {'i': d})
def editaddon(request):
    id=request.POST['id']
    data=Addaddon.objects.get(id=id)
    return render(request,'editaddon.html',{'d':data})
def updateaddon(request):
    id=request.POST['id']
    d=Addaddon.objects.get(id=id)
    d.aname = request.POST['aname']
    d.amount = request.POST['amound']
    d.save()
    data = Addaddon.objects.all()
    return render(request, 'showaddon.html', {'d': data})
def editpackage(request):
    id=request.POST['id']
    data=Addpackage.objects.get(id=id)
    return render(request,'editpackage.html',{'d':data})
def updatepackage(request):
    id=request.POST['id']
    d=Addpackage.objects.get(id=id)

    d.pname = request.POST['pname']
    d.photo = request.FILES['file']
    d.pamount = request.POST['pamount']
    d.save()
    data = Addpackage.objects.all()
    return render(request, 'showpackage.html', {'d': data})
def out(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,'home.html')
def editmyprofile(request):
    id=request.POST['id']
    data=Register.objects.get(id=id)
    return render(request,'editmyprofile.html',{'data':data})
def updatemyprofile(request):
    id=request.POST['id']
    data=Register.objects.get(id=id)
    data.fname = request.POST['fname']
    data.lname = request.POST['lname']
    data.gender = request.POST['gender']
    data.dob = request.POST['dob']
    data.phno = request.POST['phno']
    data.email = request.POST['email']
    data.save()
    email = request.session['user']
    data = Register.objects.filter(email=email)
    return render(request,'myprofile.html', {'data': data})
def availabileflights(request):
    today=date.today()
    data = Addflightschedule.objects.filter(ddate__gt=today).all
    return render(request,'availabileflights.html',{'d':data})
def showavailabileflights(request):
    '''today=date.today()'''
    id = request.POST['id']
    data = Addflightschedule.objects.get(id=id)
    return render(request,'showavailabileflights.html',{'data':data})
def showreport(request):
    data = Register.objects.all()
    return render(request,'report.html',{'data':data})
def showclasstype(request):
    fid=request.POST['id']
    request.session['fid']=fid
    return render(request,'showclasstype.html')
def booking(request):
    id = request.POST['id']
    data = Addflightschedule.objects.get(id=id)
    return render(request,'booking.html',{'data': data})
def bookingreg(request):
    if request.method=='POST':
        addflightscheduleid = request.POST['id']
        instance = Addflightschedule.objects.get(id=addflightscheduleid)
        name=request.POST['name']
        address = request.POST['address']
        phno= request.POST['phno']
        email = request.POST['email']
        userid = request.session['user']
        data=Booking(addflightscheduleid=instance,name=name,address=address,phno=phno,status=0,email=email,userid=userid)
        data.save()
    data1=Booking.objects.filter(userid=userid)
    return render(request,'bookingdetails.html',{'book':data1})
def bookingdetails(request):
    id = request.POST['id']
    data = Booking.objects.get(id=id,status=0)
    return render(request,'bookingdetails.html', {'book': data})
def ecbooking(request):
    data = Addflightschedule.objects.get(id=request.session['fid'])
    return render(request,'ecbooking.html',{'data':data})
def booklist(request):
    id = request.session['user']
    data = Booking.objects.filter(userid=id,status=0)
    return render(request,'booklist.html', {'book': data})
def remove(request):
    id=request.POST['id']
    user=request.session['user']
    Booking.objects.filter(id=id,status=0).delete()
    data = Booking.objects.filter(userid=user)
    return render(request, 'bookingdetails.html', {'book': data})
def confirmbooking(request):
    user = request.session['user']

    Booking.objects.filter(userid=user).update(status=1)
    data=Booking.objects.filter(userid=user,status=1)
    amt=0
    for i in data:
        amt+=(i.addflightscheduleid.amount)+2000
    data=Payment(userid=user,amt=amt,date=date,fid=i.addflightscheduleid.id,status=0)
    data.save()

    return render(request,'payment.html',{'amt':amt})
def payment(request):
    user = request.session['user']
    Payment.objects.filter(userid=user).update(status=1)
    return HttpResponse("payment Successes")
def searchflight(request):
    data1 = Orgin.objects.all()
    data2 = Destination.objects.all()
    return render(request, 'searchflight.html', {'d': data2, 'o': data1})
def fsearch(request):
    '''import pdb;pdb.set_trace();'''
    org= request.POST['orgin']
    des = request.POST['destination']
    ddate = request.POST['ddate']
    sdate = datetime.strptime( ddate, '%Y-%m-%d')
    dayno = sdate.weekday()
    if dayno == 0:
        wday = 'Mon'
    if dayno == 1:
        wday = 'Tue'
    if dayno == 2:
        wday = 'Wed'
    if dayno == 3:
        wday = 'Thu'
    if dayno == 4:
        wday = 'Fri'
    if dayno == 5:
        wday = 'Sat'
    if dayno == 6:
        wday = 'Sun'
    data = Addflightschedule.objects.filter(orgin=org, destination=des, dday=wday)
    for x in data:
        print(x)
        td = datetime.strptime(ddate, '%Y-%m-%d')
    return render(request, 'availabileflights.html', {'d': data, 'ddate': ddate})


