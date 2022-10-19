from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
import pyrebase
# Create your views here.
class Sign_in_Sign_up:
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
    def home(request):
        if (request.method == 'POST'):
            form = Login(request.POST)

            if (form.is_valid()):
                email = form.cleaned_data['email_id']
                passwd = form.cleaned_data['passwd']
                sign_in = Sign_in_Sign_up()
                try:
                    sign_in.authorize.sign_in_with_email_and_password(email, passwd)
                    return render(request, 'home.html', {'option': email})
                except Exception:
                    return HttpResponse("Exception")


            else:
                return HttpResponse("Login Failed")
        return render(request,'home.html')

    def register(request):
        if(request.method=='POST'):
            form=Register(request.POST)
            if(form.is_valid()):
                sign_up=Sign_in_Sign_up()
                email=form.cleaned_data['email_id']
                passwd=form.cleaned_data['passwd']
                re_passwd=form.cleaned_data['re_password']

                if(passwd==re_passwd):
                    sign_up.authorize.create_user_with_email_and_password(email,passwd)
                    return HttpResponse("<script>alert('Registered successfully')</script>")
                else:
                    return HttpResponse("<script>alert('password does not match')</script>")



