from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .bus_data import *
from django.shortcuts import redirect
from django.contrib import messages
import pyrebase

# Create your views here.

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
firebase=pyrebase.initialize_app(firebaseConfig)
authorize=firebase.auth()
session=""
email=""
bus_list=Data_set.data
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
                session=user_auth['idToken']
                print(session)
                return render(request, 'home.html', {'option': email,'session':session})
            except Exception:
                return HttpResponse("Exception")
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request,'home.html',{'option': email,'session':session})

def register(request):
    if(request.method=='POST'):
        form=Register(request.POST)
        if(form.is_valid()):

            email=form.cleaned_data['email_id']
            passwd=form.cleaned_data['passwd']
            re_passwd=form.cleaned_data['re_password']

            if(passwd==re_passwd):
                authorize.create_user_with_email_and_password(email,passwd)
                return HttpResponse("<script>alert('Registered successfully')</script>")
            else:
                return HttpResponse("<script>alert('password does not match')</script>")
def signout(request):
    global email
    email=""
    global session
    session=""
    return render(request,'home.html',{'option': email,'session':session})

"""                                bus                                                     """

def search_bus(request):
    global bus_list
    if(request.method=="POST"):
        depature=request.POST.get('depature')
        arrive=request.POST.get('arrive')
        date=request.POST.get('date')

        try:
            fee=[]
            name=[]

            if(bus_list[depature][arrive]):
                temp=bus_list[depature][arrive]
                for i in range(len(temp)):
                    if(i%2==0):
                        fee.append(temp[i])
                    else:
                        name.append(temp[i])

                return render(request,'searchbus.html',{
                    'depature':depature,
                    'arrive':arrive,
                    'date':date,
                    'datas':zip(fee,name)})
        except:
            return render(request,'404.html')
    else:
        return render(request,'404.html')



