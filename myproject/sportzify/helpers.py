
from django.conf import settings
from twilio.rest import Client
import random


class MessageHandler:
    phone=None
    otp=None
    def __init__(self,phone,otp) -> None:
        self.phone=phone
        self.otp=otp
    def send_otp_via_message(self):     
        client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(
                                body=f'your otp is {self.otp}',
                                from_='+13854628112',
                                to=self.phone
                                )