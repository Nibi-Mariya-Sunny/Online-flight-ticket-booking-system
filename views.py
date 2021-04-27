from django.shortcuts import render
from django . http import HttpResponse
from datetime import date
from.models import Register,Login,Addflightname,Orgin,Destination,District,Flightrate,Addflightschedule,Addaddon,Addpackage,Booking
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
    ddate = request.POST['ddate']
    dtime = request.POST['dtime']
    adate = request.POST['adate']
    atime = request.POST['atime']
    amount = request.POST['amount']
    camount=int(amount)-300
    iamount=int(amount)-500
    wsamount=int(amount)+500
    bcamount =int(amount)+2000
    weight = request.POST['weight']
    data = Addflightschedule(addflightnameid=instance, orgin=orgin, destination=destination, ddate=ddate, dtime=dtime, adate=adate,
                             atime=atime,amount=amount,camount=camount,iamount=iamount, wsamount=wsamount,bcamount=bcamount,weight=weight)
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
    data=State.objects.all()
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
    data = Addplace.objects.all()
    return render(request,'showplaces.html',{'d':data})
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
    id=request.POST['id']
    data=Addflightschedule.objects.get(id=id)
    return render(request,'editflightschedule.html',{'d':data})
def updateflightschedule(request):
    id=request.POST['id']
    d=Addflightschedule.objects.get(id=id)
    d.fname = request.POST['fname']
    d.orgin.orgin = request.POST['orgin']
    d.destination.destination = request.POST['destination']
    d.ddate = request.POST['ddate']
    d.dtime = request.POST['dtime']
    d.adate = request.POST['adate']
    d.atime = request.POST['atime']
    d.save()
    data = Addflightschedule.objects.all()
    return render(request, 'showflightschedule.html', {'d': data})
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
    data = Addflightschedule.objects.get(id=request.session['fid'])
    return render(request,'booking.html',{'data':data})
def bookingreg(request):
    addflightscheduleid = request.POST['id']
    instance = Addflightschedule.objects.get(id=addflightscheduleid)
    name=request.POST['name']
    address = request.POST['address']
    phno= request.POST['phno']
    email = request.POST['email']
    userid = request.session['user']
    data=Booking(addflightscheduleid=instance,name=name,address=address,phno=phno,email=email,userid=userid)
    data.save()
    data1=Booking.objects.filter(userid=userid)
    return render(request,'bookingdetails.html',{'book':data1})
def bookingdetails(request):
    id = request.POST['id']
    data = Booking.objects.get(id=id)
    return render(request,'bookingdetails.html', {'book': data})
def ecbooking(request):
    data = Addflightschedule.objects.get(id=request.session['fid'])
    return render(request,'ecbooking.html',{'data':data})

