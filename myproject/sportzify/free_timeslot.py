from datetime import datetime,timedelta,timezone
import time
import schedule
from django.core.management.base import BaseCommand

from django.shortcuts import render, redirect
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
settings.configure()

def free_timeslot():
    print("Deleting old bookings...")
    return redirect("delete_time_slots")
    

    

# Schedule the task to run at 12:00 am every day
schedule.every().day.at("16:59").do(free_timeslot)

while True:
    schedule.run_pending()
    time.sleep(1)
    