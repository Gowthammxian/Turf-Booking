
from django.shortcuts import render
import random
from django.shortcuts import render, redirect
import razorpay
from .forms import *
from .helpers import MessageHandler
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
from .models import *
import random
from django.http import HttpResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt

from .forms import *
# Create your views here.

def delete_time_slots(request):
    Timeslot.objects.all().delete()
    return HttpResponse("Timeslot Deleted")

def home(request):
    context={}
    return render(request,"sportzify/home.html",context)

def loginpage(request):
    form= Formcreate()
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')

        try:
            result=customer.objects.get(username=uname)
            name=result.username
            password=result.password
            if uname==name and password==passw:
                return redirect('/customer/{}'.format(result.uid))

        except:
            message="Invalid credentials check your data"
            return render(request,"sportzify/login.html",{'message':message})
    context = {'form':form}
    return render(request, 'sportzify/login.html',context)

def registerpage(request):
    form= Formcreate()
    
    if request.method=='POST':
        username=request.POST.get('username')
        aadhar=request.POST.get('aadhar')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if len(aadhar) != 12 or password != password2:
            message="Please enter a valid details!!!"
            return render(request,"sportzify/register.html",{'message':message,'form':form})
        
            
        
        else:
            forms=Formcreate(request.POST)
            if forms.is_valid():
                forms.save()
                profile=customer.objects.get(username=username)
                profile.otp=random.randint(1000,9999)
                profile.save()
                phone=profile.phone
                message_handler=MessageHandler(phone,profile.otp).send_otp_via_message()   
                return redirect('/otp/{}'.format(profile.uid))
    context = {'form':form}
    return render(request,'sportzify/register.html',context)


def otp(request,uid):
    form=Formcreate()
      
    
    if request.method=='POST':

        otp=request.POST.get('otp')
        res=customer.objects.get(uid=uid)
        otp=res.otp
        if otp==otp:
            messages.success(request, "Your profile is updated successfully!")
            return redirect('login')

        else:
            return redirect(f'/otp/{uid}')

    return render(request,'sportzify/otp.html',{'form':form})

def admin_login(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_mainpage')
        else:
            message="Invalid credentials check your data"
            return render(request,"sportzify/admin_login.html",{'message':message})

    return render(request,"sportzify/admin_login.html")

def customer_home(request,uid):
    items= None
    item=None
    if request.method == "POST":
        location=request.POST.get('location')
        ground_type=request.POST.get('ground_type')
        print(ground_type)
        print(location)
        
        if ground_type == '':
            location_turf = Turf.objects.filter(turf_address=location)
            items = sorted(location_turf, key=lambda x: x.turf_name)
            
        else:
            location_turf = Turf.objects.filter(Q(turf_address=location) & Q(ground_type=ground_type))
            items = sorted(location_turf, key=lambda x: x.turf_name)
    else:   
        all_turf=Turf.objects.all()
        item = sorted(all_turf, key=lambda x: x.turf_name)
    context={'uid':uid,'location_turfs':items,'all_turfs':item}
    return render(request,"sportzify/customer.html",context)

def admin_mainpage(request):
    
    book_details=Booking.objects.all()
    

    return render(request,"sportzify/admin_mainpage.html",{'book_details':book_details})

def adding_turf(request):
    form = TurfForm()
    if request.method=="POST":
        name=request.POST.get('turf_name')
        forms=TurfForm(request.POST,request.FILES)
        print(forms)
        if forms.is_valid():
            forms.save()
            print("saved")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field {field}: {error}")
    context = {'form':form}
    return render(request,"sportzify/adding_turf.html",context)


def About(request):

    return render(request,"sportzify/About.html")

def turf_detail(request,uid,turf_uid):

    turf_details=Turf.objects.get(turf_uid=turf_uid)
    review = ReviewRating.objects.filter(turf_uid=turf_details)
    for i in review:
        print(i.reviews)
    context={'turf_details':turf_details,'uid':uid,'turf_uid':turf_uid,'review':review}
    return render(request,"sportzify/turf_detail.html",context)   

from datetime import datetime
import pytz
IST=pytz.timezone('Asia/Kolkata')

def booking(request,turf_uid,uid):
    date_value = request.POST.get('date')
    print(date_value)
    total=None
    time_list=[]
    turf_details = Turf.objects.get(turf_uid=turf_uid)
    check_time=Timeslot.objects.filter(turf_uid=turf_details) 
    
         
    print(time_list)     
    customer_details = customer.objects.get(uid=uid)
    
    if request.method=="POST":
    
        no_person=request.POST.get('persons')
        date=request.POST.get('date')
        date=date
        time=request.POST.getlist('time')
        booking_time=datetime.now()
        cost=turf_details.cost_per_hr
        count=len(time)
        total=int(count)*int(cost)
        print(total)
        print("total")
        
        book=Booking.objects.create(uid=customer_details,turf_uid=turf_details,person_count=no_person,t_and_d=date,time_slot=time)
        for i in time:
            Timeslot.objects.create(turf_uid=turf_details,time=i,date=date)
            
    
      
        context={'date_value':date_value,'turf_uid':turf_uid,'uid':uid,'turf_details':turf_details,'customer_details':customer_details,'time_list':time_list,'total':total}
        
        
        
    for i in check_time:
        time_list.append((i.time+i.date))   
    context={'date_value':date_value,'turf_uid':turf_uid,'uid':uid,'turf_details':turf_details,'customer_details':customer_details,'time_list':time_list,'total':total}
    return render(request,"sportzify/booking.html",context)


def payment(request,turf_uid,uid,total):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000
        
        client = razorpay.Client(
            auth=("rzp_test_d8KZMdlY59Fi22", "LQW1zo3hrcHIH5bcMDKWx9l1"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    context={'total':int(total) * int(100)}
    
        
        
    return render(request,'sportzify/payment.html',context)

@csrf_exempt
def success(request):
    return render(request,'sportzify/success.html')
    
def submit_review(request,turf_uid,uid):
    user=customer.objects.get(uid=uid)
    turf=Turf.objects.get(turf_uid=turf_uid)
    if request.method == "POST":
        rate = request.POST.get('rating')
        review = request.POST.get('review')
        
        ReviewRating.objects.create(uid=user,turf_uid=turf,rating=rate,reviews=review)
        review = ReviewRating.objects.filter(turf_uid=turf)
        context={'turf_details':turf,'uid':uid,'turf_uid':turf_uid,'review':review}
        return render(request,"sportzify/turf_detail.html",context)
        
        
        
def basketball(request):
    return render(request,"sportzify/basketball.html")


def callback(request):
    return render(request,"sportzify/callback.html")

def viewbooking(request):
    turfs=Turf.objects.all()
    bookings=None
    if request.method=="POST":
        turf_id=request.POST.get('turf')
        turf=Turf.objects.get(turf_uid=turf_id)
        bookings=Booking.objects.filter(turf_uid=turf)
    
    
    
    return render(request,"sportzify/viewbooking.html",{'turf':turfs,'bookings':bookings})

def allturf(request):
    all_turf=None
    if request.method=="POST":
        turf_id=request.POST.get('turf')
        all_turf=Turf.objects.filter(turf_uid=turf_id)
        print(all_turf)
        
    else:
        all_turf=Turf.objects.all()
        
    items = sorted(all_turf, key=lambda x: x.turf_name)
    return render(request,"sportzify/allturf.html",{'all_turf':items})

def confirm(request,turf_uid,turf_name):
    if request.method=="POST":
        delete_turf=Turf.objects.get(turf_uid=turf_uid)
        delete_turf.delete()
        return redirect('allturf')
    
    return render(request,"sportzify/confirmation.html",{'turf_name':turf_name})

def booked_history(request,uid):
    user_id=customer.objects.get(uid=uid)
    Book_details=Booking.objects.filter(uid=user_id)
    
    
    
    return render(request,"sportzify/history.html",{'uid':uid,'details':Book_details})

from datetime import datetime, timedelta
def delete_confirm(request,id,uid):
    if request.method=="POST":
        delete_book=Booking.objects.get(id=id)
        delete_book.delete()
        return redirect('history',uid)
    
    return render(request,"sportzify/delete_confirm.html")      


def customer_details(request):
    customer_details=customer.objects.all()
    context={'cust_details':customer_details}
    return render(request,"sportzify/customer_details.html",context)
        


