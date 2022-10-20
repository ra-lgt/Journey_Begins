from django.shortcuts import render
from .bus_data import Data_set

# Create your views here.
bus_list=Data_set().data

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

