from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('log',views.log,name='log'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('reg',views.reg,name='reg'),
    path('Userhome',views.Userhome,name='Userhome'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('report', views.report, name='report'),
    path('addflightname', views.addflightname, name='addflightname'),
    path('addfname', views.addfname, name='addfname'),
    path('addflightschedule', views.addflightschedule, name='addflightschedule'),
    path('addfschedule', views.addfschedule, name='addfschedule'),
    path('addflightrate', views.addflightrate, name='addflightrate'),
    path('addfrate', views.addfrate, name='addfrate'),
    path('addplace', views.addplace, name='addplace'),
    path('placereg', views.placereg, name='placereg'),
    path('adddistrict', views.adddistrict, name='adddistrict'),
    path('districtreg', views.districtreg, name='districtreg'),
    path('addaddon', views.addaddon, name='addaddon'),
    path('addonreg', views.addonreg, name='addonreg'),
    path('addpackage', views.addpackage, name='addpackage'),
    path('packagereg', views.packagereg, name='packagereg'),
    path('showflightname', views.showflightname, name='showflightname'),
    path('showflightschedule', views.showflightschedule, name='showflightschedule'),
    path('showflightrate', views.showflightrate, name='showflightrate'),
    path('showplaces', views.showplaces, name='showplaces'),
    path('showdistrict', views.showdistrict, name='showdistrict'),
    path('showaddon', views.showaddon, name='showaddon'),
    path('showaddon', views.showaddon, name='showaddon'),
    path('showpackage', views.showpackage, name='showpackage'),
    path('editflightname', views.editflightname, name='editflightname'),
    path('update', views.update, name='update'),
    path('editflightschedule', views.editflightschedule, name='editflightschedule'),
    path('updateflightschedule', views.updateflightschedule, name='updateflightschedule'),
    path('editaddon', views.editaddon, name='editaddon'),
    path('updateaddon', views.updateaddon, name='updateaddon'),
    path('editpackage', views.editpackage, name='editpackage'),
    path('updatepackage', views.updatepackage, name='updatepackage'),
    path('showregisteredusers', views.showregisteredusers, name='showregisteredusers'),
    path('out', views.out, name='out'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('editmyprofile', views.editmyprofile, name='editmyprofile'),
    path('updatemyprofile', views.updatemyprofile, name='updatemyprofile'),
    path('availabileflights', views.availabileflights, name='availabileflightse'),
    path('showavailabileflights', views.showavailabileflights, name='showavailabileflights'),
    path('showreport', views.showreport, name='showreport'),
    path('showclasstype', views.showclasstype, name='showclasstype'),
    path('booking', views.booking, name='booking'),
    path('bookingreg', views.bookingreg, name='bookingreg'),
    path('bookingdetails', views.bookingdetails, name='bookingdetails'),
    path('ecbooking', views.ecbooking, name='ecbooking'),
    path('booklist', views.booklist, name='booklist'),
    path('remove', views.remove, name='remove'),
    path('confirmbooking', views.confirmbooking, name='confirmbooking'),
    path('payment', views.payment, name='payment'),
]
