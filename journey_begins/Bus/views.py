from django.shortcuts import render
from .bus_data import Data_set
import time
from datetime import date as dates
import random
from django.http import HttpResponse
# Create your views here.



bus_list=Data_set().data
curr_time=time.gmtime()

#bus_data
name=[]
fare=[]
s_point=[]
e_point=[]
bus_type=[]
bus=""
start=[]
end=[]
offers=[]
seats=[]
depature=""
arrive=""
date=""
def search_bus(request):

    global name
    global fare
    global s_point
    global e_point
    global bus_type
    global bus
    global start
    global end
    global offers
    global seats
    global depature
    global arrive
    global date

    if(request.method=="POST"):
        depature=request.POST.get('depature').strip().title()
        arrive=request.POST.get('arrive').strip().title()
        date=request.POST.get('date')

        input_date=date.split("-")
        a=str(dates.today())
        curr_date=a.split("-")

        if(input_date[0]<curr_date[0]):
            return render(request,'404.html')

        elif(input_date[1]<curr_date[1]):
            return render(request, '404.html')
        elif(input_date[2]<curr_date[2] and input_date[1]==curr_date[1]):
            return render(request, '404.html')


        try:
            curr_hour=curr_time.tm_hour
            if(bus_list[depature][arrive]):

                bus=(bus_list[depature][arrive])
                
                name = (bus_list[depature][arrive]['name'])
                fare = (bus_list[depature][arrive]['fare'])
                s_point = (bus_list[depature][arrive]['s_point'])
                e_point = (bus_list[depature][arrive]['e_point'])
                bus_type = (bus_list[depature][arrive]['bus_type'])

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

            for k in fare:
                t=random.choice([10,20,12,15,5,7,19])
                offers.append(k-t)

            for m in range(len(name)):
                seats.append(random.choice([20,30,40,50,45,35]))

            return render(request,'searchbus.html',{
                'depature':depature,
                'arrive':arrive,
                'date':date,
                'length':len(name),
                'datas':zip(name,fare,s_point,e_point,start,end,bus_type,offers,seats)
                })
        except:
            return render(request,'404.html')
    else:
        return render(request,'404.html')



def bus_filter_Ac(request):
    global name
    global fare
    global s_point
    global e_point
    global bus_type
    global bus
    global start
    global end
    global offers
    global seats
    global depature
    global arrive
    global date
    
    Ac_name=[]
    Ac_fare=[]
    Ac_s_point=[]
    Ac_e_point=[]
    Ac_bus_type=[]
    Ac_end=[]
    Ac_start=[]
    Ac_offers=[]
    Ac_seats=[]
    count=0
    
    for i in bus['bus_type']:
        if(i=='Ac'):
            Ac_name.append(bus['name'][count])
            Ac_fare.append(bus['fare'][count])
            Ac_s_point.append(bus['s_point'][count])
            Ac_e_point.append(bus['e_point'][count])
            Ac_bus_type.append(i)
            Ac_start.append(start[count])
            Ac_end.append(end[count])
            Ac_offers.append(offers[count])
            Ac_seats.append(offers[count])
            count+=1
        else:
            count+=1


    return render(request,'searchbus.html',{
     'depature':depature,
     'arrive':arrive,
     'date':date,
     'length':len(name),
     'datas':zip(Ac_name,Ac_fare,Ac_s_point,Ac_e_point,Ac_start,Ac_end,Ac_bus_type,Ac_offers,Ac_seats)
     })

def bus_filter_Nc(request):
    global name
    global fare
    global s_point
    global e_point
    global bus_type
    global bus
    global start
    global end
    global offers
    global seats
    global depature
    global arrive
    global date

    Ac_name=[]
    Ac_fare=[]
    Ac_s_point=[]
    Ac_e_point=[]
    Ac_bus_type=[]
    Ac_end=[]
    Ac_start=[]
    Ac_offers=[]
    Ac_seats=[]
    count=0

    for i in bus['bus_type']:
        if(i=='Nc'):
            Ac_name.append(bus['name'][count])
            Ac_fare.append(bus['fare'][count])
            Ac_s_point.append(bus['s_point'][count])
            Ac_e_point.append(bus['e_point'][count])
            Ac_bus_type.append(i)
            Ac_start.append(start[count])
            Ac_end.append(end[count])
            Ac_offers.append(offers[count])
            Ac_seats.append(offers[count])
            count+=1
        else:
            count+=1


    return render(request,'searchbus.html',{
     'depature':depature,
     'arrive':arrive,
     'date':date,
     'length':len(name),
     'datas':zip(Ac_name,Ac_fare,Ac_s_point,Ac_e_point,Ac_start,Ac_end,Ac_bus_type,Ac_offers,Ac_seats)
     })










