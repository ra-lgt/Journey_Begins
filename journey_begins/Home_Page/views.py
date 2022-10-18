from django.shortcuts import render
from django.http import HttpResponse
from .forms import Register
# Create your views here.
def home(request):
    if(request.method=='POST'):
        form=Register(request.POST)

        if(form.is_valid()):
            email=form.cleaned_data['email_id']
            return HttpResponse(email)

    else:
        return render(request,'home.html')
def login(request):
    return HttpResponse("hiii")



