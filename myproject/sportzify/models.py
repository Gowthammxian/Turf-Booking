from datetime import datetime
from django.db import models
import uuid
from django.utils import timezone


# Create your models here.

class customer(models.Model):
    username=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=20,null=True)
    uid=models.UUIDField(default=uuid.uuid4)
    otp=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True)
    password2=models.CharField(max_length=50,null=True)
    aadhar=models.CharField(max_length=12,null=True)

    def __str__(self) :
        return self.username

class Turf(models.Model):
    GROUND = (
    ("--Select Ground Type--","--Select Ground Type--"),
    ("Cricket", "Cricket"),
    ("Football", "Football"),
    ("Basketball", "Basketball"),
    ("Tennis", "Tennis"),
    ("Batminton", "Batminton"),
    ("Hockey", "Hockey"),
    )
    
    turf_uid=models.UUIDField(default=uuid.uuid4)
    turf_name=models.CharField(max_length=200,null=True)
    turf_address=models.CharField(max_length=200,null=True)
    turf_phone=models.CharField(max_length=200,null=True)
    turf_email=models.CharField(max_length=200,null=True)
    cost_per_hr=models.CharField(max_length=10,null=True)
    description=models.CharField(max_length=1000,null=True)
    ground_type=models.CharField( max_length = 50,
        choices = GROUND,default="Select Ground Type")
    turf_image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.turf_name

    @property
    def imageURL(self):
        try:
            url = self.turf_image.url
        except:
            url=''
        return url
    
class Timeslot(models.Model):
    
    turf_uid=models.ForeignKey(Turf,null=True,on_delete=models.CASCADE)
    time = models.CharField(max_length=50,null=True)
    date=models.CharField(max_length=200,null=True)
    
    def __str__(self) -> str:
        return self.time
    


class Booking(models.Model):
    uid=models.ForeignKey(customer,null=True,on_delete=models.CASCADE)
    turf_uid=models.ForeignKey(Turf,null=True,on_delete=models.CASCADE)
    person_count=models.CharField(max_length=200,null=True)
    t_and_d=models.CharField(max_length=100,null=True)
    time_slot=models.CharField(max_length=50,null=True)
    booking_time=models.DateTimeField(default=datetime.now())
    
class ReviewRating(models.Model):
    uid=models.ForeignKey(customer,null=True,on_delete=models.CASCADE)
    turf_uid=models.ForeignKey(Turf,null=True,on_delete=models.CASCADE)
    reviews = models.TextField(max_length=500,blank=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.uid.username  
    

class Coffee(models.Model):
    uid=models.ForeignKey(customer,null=True,on_delete=models.CASCADE)
    turf_uid=models.ForeignKey(Turf,null=True,on_delete=models.CASCADE)
    amount = models.CharField(max_length=100 , blank=True)
    razorpay_payment_id = models.CharField(max_length=1000 ,blank=True)
    paid = models.BooleanField(default=False)
    







