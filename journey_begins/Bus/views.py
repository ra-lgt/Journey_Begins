from django.shortcuts import render
from .bus_data import Data_set
import time
from datetime import date as dates
import random
# Create your views here.
bus_list=Data_set().data
curr_time=time.gmtime()


def search_bus(request):
    global hours
    start_time=0
    if(request.method=="POST"):
        depature=request.POST.get('depature')
        arrive=request.POST.get('arrive')
        date=request.POST.get('date')

        input_date=date.split("-")
        a=str(dates.today())
        curr_date=a.split("-")

        if(input_date[0]<curr_date[0]):
            return render(request,'404.html')
        else:
            if(input_date[1]<curr_date[1]):
                return render(request, '404.html')
            elif(input_date[2]<curr_date[2]):
                return render(request, '404.html')


        try:
            fee=[]
            name=[]
            start=[]
            end=[]
            offers=[]

            curr_hour=curr_time.tm_hour


            if(bus_list[depature][arrive]):
                temp=bus_list[depature][arrive]
                for i in range(len(temp)):
                    if(i%2==0):

                        name.append(temp[i])
                    else:
                        offers.append(temp[i] - random.choice([20, 30, 15, 9, 2, 6, 8, 16,20,11.5]))
                        fee.append(temp[i])
                for i in range(len(name)):
                    start_time=curr_hour+random.randint(1,5)
                    if(start_time>24):
                        start_time=abs(start_time-24)
                    start.append((start_time))

                for j in start:
                    end_time=j+random.randint(1,5)
                    if(end_time>24):
                        end_time=abs(end_time-24)
                    end.append(end_time)
                print(end)
                print(start)

                return render(request,'searchbus.html',{
                    'depature':depature,
                    'arrive':arrive,
                    'date':date,
                    'datas':zip(name,fee,start,end,offers)})
        except:
            return render(request,'404.html')
    else:
        return render(request,'404.html')

