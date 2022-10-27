import firebase_admin
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from instamojo_wrapper import Instamojo
from .forms import *
import smtplib
from journey_begins import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from firebase_admin import firestore
from firebase_admin import credentials

from django.shortcuts import redirect
from django.contrib import messages
import pyrebase

# Create your views here.
API_KEY="test_e4152152589c3c8954a56998ef1"
AUTH_TOKEN="test_16d4fce2079a45ec988e3655747"

insta_mojo=Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

firebaseConfig = {
        "apiKey": "AIzaSyAEzl4aWGVQnTb4Sk9pMNRhzNCxe3MFAmw",

        "authDomain": "sece-hackathon-390a0.firebaseapp.com",

        "projectId": "sece-hackathon-390a0",

        "storageBucket": "sece-hackathon-390a0.appspot.com",

        "databaseURL":"https://sece-hackathon-390a0-default-rtdb.firebaseio.com/",

        "messagingSenderId": "772188818031",

        "appId": "1:772188818031:web:1d02b48b391ce1602b9b9a",

        "measurementId": "G-Y5YXYRMD9M"

    }

#firestore

#database and auth
firebase=pyrebase.initialize_app(firebaseConfig)
authorize=firebase.auth()
storage=firebase.storage()
database=firebase.database()
session=""
email=""
Member_ship_type=""

#membership
member_email=""
f_name=""
l_name=""
mobile=""
age=""


def home(request):

    global session
    global email

    if (request.method == 'POST'):
        form = Login(request.POST)

        if (form.is_valid()):
            email = form.cleaned_data['email_id']
            passwd = form.cleaned_data['passwd']

            try:
                user_auth=authorize.sign_in_with_email_and_password(email, passwd)
                session+=user_auth['idToken']

                return render(request, 'home.html', {'option': email.replace("@gmail.com",""),'session':session})
            except Exception:
                return HttpResponse("Try again turn on wifi or user doesn't exists")
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request,'home.html',{'option': email.replace("@gmail.com",""),'session':session})

def register(request):
    if(request.method=='POST'):
        form=Register(request.POST)
        if(form.is_valid()):

            emails=form.cleaned_data['email_id']
            passwd=form.cleaned_data['passwd']
            re_passwd=form.cleaned_data['re_password']

            if(passwd==re_passwd):
                try:
                    authorize.create_user_with_email_and_password(emails,passwd)
                except:
                    return HttpResponse("user already exists")
                message=MIMEMultipart('alternative')
                message['subject']="Thanks for registering"
                message["from"]="raviajay9344@gmail.com"
                message["to"]=emails

                html="""\
                <html>
                <head>
                    <link href="https://fonts.googleapis.com/css?family=Kaushan+Script|Source+Sans+Pro" rel="stylesheet">
                    <style>
                    body {
                        background: #e2e1e0;
                        text-align: center;
                      }

                      .card {
                        background: #fff;
                        border-radius: 2px;
                        display: inline-block;
                        height: 600px;
                        margin: 1rem;
                        position: relative;
                        width: 800px;
                      }.card-5 {
                        box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(245, 157, 6, 0.866);
                      }
                      h1{
                        font-family: 'Kaushan Script', cursive;
                      font-size:4em;
                      letter-spacing:3px;
                      color: rgba(245, 157, 6, 0.866);
                      margin:0;
                      margin-bottom:20px;
                    }
                    </style>
                </head>
                <body>

                    <div class="card card-5">
                        <h1>Your Journey Begins !</h1>
                        <p style="font-weight:bold;text-align:left;padding-left:40px;padding-top:30px;font-size:20px;">Hi user,</p>
                        <p style="padding-left:60px;padding-top:10px;font-size:20px;">We're so happy to have you on board! Be sure to stay logged in for effortless<br><p style="padding-right:380px;font-size:20px;">booking experience.</p></p>
                        <p style="padding-right:600px;padding-top:30px;font-weight:bold;font-size:18px;">Regards,</p>
                        <p style="padding-right:550px;font-weight:bold;font-size:18px;">Journey Begins !</p>
                        <p style="font-weight:300;padding-top:50px;padding-right:50px">Please do not hesitate to call us on at +91-9244262900(Mon-Fri 10AM - 6.30PM, Sat 10AM - 4.00PM)</p>
                        <p style="font-weight:300;padding-bottom:70px;padding-right:130px">or email customercare@journeybegins.com if have any questions at all regarding the above.</p>
                    </div>
                    </body>
                    </html>
                """
                html_mail=MIMEText(html,'html')
                message.attach(html_mail)

                server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                server.login("raviajay9344@gmail.com","vmrxmwpnrruyonus")
                server.sendmail("raviajay9344@gmail.com",emails,message.as_string())

                server.quit()
                return HttpResponse("<script>alert('Registered successfully')</script>")
            else:
                return HttpResponse("<script>alert('password does not match')</script>")
def signout(request):
    global email
    email=""
    global session
    session=""
    return render(request,'home.html',{'option': email,'session':session})


def cancel_reservation(request):
    #if(session==""):
     #   return HttpResponse("Login to cancel_reservation :)")
    #if(request.method=='POST'):

    if(request.method=='POST'):
        user_name=request.POST.get('name')

        emails = request.POST.get('emails')
        bus = request.POST.get('bus')
        desc = request.POST.get('desc')

        data={
            'name':user_name,
            'bus':bus,
            'email':emails,
            'desc':desc
        }
        database.push(data)
    return render(request,'cancel_reservation.html')

def contactus(request):
    if(request.method=='POST'):
        #name=request.POST.get('name')
        #num=request.Post.get('num')
        #emails=request.Post.get('email')
        #subject=request.Post.get('subject')
        #message=request.Post.get('message')

        return HttpResponse("""<h1>We will shortly contact you</h1>""")


    return render(request,'contact_us.html')

def subscription(request):
    return render(request,'subscription.html')

def payment_success(request):
    global member_email,f_name,l_name,mobile,age,Member_ship_type
    req_id=request.GET.get('payment_id')
    data = {
        'f_name': f_name,
        'l_name': l_name,
        'member_email': member_email,
        'mobile': mobile,
        'age': age,
        'Membership':Member_ship_type,
        'payment_id':req_id,
    }

    settings.fire.collection('membership').add(data)
    return HttpResponse("success")

def gold_membership(request):

    global insta_mojo,member_email,f_name,l_name,mobile,age,Member_ship_type
    if(request.method=='POST'):
        member_email=request.POST.get('email')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        mobile=request.POST.get('mobile')
        age=request.POST.get('age')
        Member_ship_type="GOLD Membership"
        response=insta_mojo.payment_request_create(
            purpose='Gold Membership',
            amount=7500,
            buyer_name='journey_begins_admin',
            email='raviajay9344@gmail.com',
            redirect_url='http://127.0.0.1:8000/payment_success')
        return render(request,'membership.html',context={'url':response['payment_request']['longurl'],'amount':7500})

    return render(request,'membership.html',{'amount':7500,'url':""})

def silver_membership(request):
    global insta_mojo, member_email, f_name, l_name, mobile, age, Member_ship_type
    if (request.method == 'POST'):
        member_email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        Member_ship_type = "Silver"
        response = insta_mojo.payment_request_create(
            purpose='Silver Membership',
            amount=5000,
            buyer_name='journey_begins_admin',
            email='raviajay9344@gmail.com',
            redirect_url='http://127.0.0.1:8000/payment_success')
        return render(request, 'membership.html', context={'url': response['payment_request']['longurl'], 'amount': 5000})

    return render(request, 'membership.html', {'amount': 5000, 'url': ""})

def vip_membership(request):
    global insta_mojo, member_email, f_name, l_name, mobile, age, Member_ship_type
    if (request.method == 'POST'):
        member_email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        Member_ship_type = "VIP"
        response = insta_mojo.payment_request_create(
            purpose='Vip membership',
            amount=10000,
            buyer_name='journey_begins_admin',
            email='raviajay9344@gmail.com',
            redirect_url='http://127.0.0.1:8000/payment_success')
        return render(request, 'membership.html', context={'url': response['payment_request']['longurl'], 'amount': 10000})

    return render(request, 'membership.html', {'amount': 10000, 'url': ""})

def your_tickets(request):
    global email
    my_ticket=settings.fire.collection("Tickets").get()
    ticket_email=[]
    ticket_date=[]
    ticket_phone=[]
    ticket_count=[]
    ticket_from=[]
    ticket_id=[]
    ticket_pass_name=[]
    for i in my_ticket:
        dicts=i.to_dict()
        if(dicts['email']==email):
            ticket_email.append(dicts['email'])
            ticket_date.append(dicts['date'])
            ticket_phone.append(dicts['phone'])
            ticket_from.append(dicts['from'])
            ticket_id.append(dicts['ticket_id'])
            ticket_pass_name.append(dicts['name'])
    print(ticket_email)
    print(ticket_date)
    print(ticket_from)
    return HttpResponse("success")
