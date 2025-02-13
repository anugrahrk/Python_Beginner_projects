from email.message import EmailMessage
import random
import string
import ssl
import smtplib
from config import email_password
def random_otp():
    otp=''.join(random.choices(string.digits,k=6))
    return otp
def sent_otp_mail():
    email_sender='demouserprojectrun@gmail.com'
    email_reciever='xyn5w8zid9@zvvzuv.com'
    otp=random_otp()
    subject="Your OTP Code"
    body=f"""
    Hello,
            Your Otp code is : {otp}

    Thank you for Using #
    
     """
    em=EmailMessage()
    em['Subject']=subject
    em['From']=email_sender
    em['To']=email_reciever
    em.set_content(body)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())
        print(f"Otp send to {email_reciever} successfully.")

    
sent_otp_mail()

    
