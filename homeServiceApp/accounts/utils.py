from django.core.mail import send_mail
from django.conf import settings
import random




def generate_otp():
    return str(random.randint(100000, 999999))
def send_otp_email(user_email, otp):
    subject = 'Your OTP Verification Code'
    message = f'Your OTP code is {otp}. It will expire in 5 minutes.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)


def send_welcome_email(user_email, first_name, username):
    subject = 'Welcome to Hire Up'
    message = 'Dear {},\n'+'Welcome to HireUp! We\'re thrilled to have you on board and excited for the journey ahead. Your account has been successfully created and your username is {}, and you\'re now part of a growing community dedicated to making the hiring process easier and more efficient.\n'+'To start exploring, here are a few things you can do:\n'+'If you did not create this account, please let us know immediately by replying to this email or reaching out to our support team at [support@hireup.com]. We\'ll take the necessary steps to secure your information.\n'+'Thank you for joining us!'.format(first_name, username)
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)