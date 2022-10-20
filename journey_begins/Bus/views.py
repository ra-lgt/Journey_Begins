from django.shortcuts import render
from .bus_data import Data_set
import time
import random
# Create your views here.
bus_list=Data_set().data
curr_time=time.gmtime()
hour=random.randint(1,5)

def search_bus(request):
    global bus_list
    global curr_time
    global hour


    start_time=0
    if(request.method=="POST"):
        depature=request.POST.get('depature')
        arrive=request.POST.get('arrive')
        date=request.POST.get('date')

        try:
            fee=[]
            name=[]
            start_time=curr_time.tm_hour+hour
            if(start_time>24):
                start_time-curr_time.tm_hour

            end_time=start_time+hour
            if(end_time>24):
                end_time-curr_time.tm_hour

            start=[]
            end=[]
            offers=[]
            mins=[]


            if(bus_list[depature][arrive]):
                temp=bus_list[depature][arrive]
                for i in range(len(temp)):
                    if(i%2==0):

                        name.append(temp[i])
                    else:
                        offers.append(temp[i] - random.choice([20, 30, 15, 9, 2, 6, 8, 16,20,11.5]))
                        fee.append(temp[i])
                for j in range(len(name)):
                    if (start_time < 0 or start_time==24):
                        start_time = 0
                    elif (start_time > 24):
                        start_time=int(curr_time.tm_hour-start_time)
                    if (end_time < 0 or end_time==24):
                        end_time = 0
                    elif (end_time > 24):
                        end_time=int(curr_time.tm_hour-end_time)
                    mins.append(random.randint(1,60))

                    start.append(abs(start_time))
                    end.append(abs(end_time))
                    start_time+=random.choice([1,2,3])
                    end_time+=random.choice([1,2,3])

                print(fee,name,start,end,offers,(mins))
                return render(request,'searchbus.html',{
                    'depature':depature,
                    'arrive':arrive,
                    'date':date,
                    'datas':zip(name,fee,start,end,offers,mins)})
        except:
            return render(request,'404.html')
    else:
        return render(request,'404.html')

