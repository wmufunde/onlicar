from django.shortcuts import render
from django.http import HttpResponse
from .models import data_table
import json
import datetime
import ast


import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'vehicles.json')
print (file_path)
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    msg=""
    if request.method == "POST":
        msg="Data populated succesfully...."
        with open(file_path) as json_data:
            d = json.load(json_data)
            #d is a list of dictionaries
            for entry in d:
                #for each dictionary in the list of dictionary
                driver_name=entry["driver_name"]
                insurance=entry["insurance"]
                tax=entry["tax"]
                mot=entry["mot"]
                phone_no=str(entry["driver_phone"])
                #print (entry["model_data"])

                model_data=ast.literal_eval(entry["model_data"]) #It's a dictioanary but is saved as string ----
                #  this converts to python dictionary.


                #for key in model_data:
                    #print key
                lastMotDate=model_data["lastMotDate"]
                model_name = model_data["additionalData"]["model"]
                #FORMATS THE DATE as Mar 21, 2017
                k = datetime.datetime.strptime(lastMotDate, "%d/%m/%Y").date()
                fmt = '%b %d, %Y'
                lastMotDate= str(k.strftime(fmt))
                if not str(phone_no).startswith("0"):
                    phone_no="0"+phone_no
                #print type(lastMotDate)

                new_obj=data_table(driver_name=driver_name,insurance=insurance,tax=tax,mot=mot,phone_no=phone_no,lastMotDate=lastMotDate,model_name=model_name)
                new_obj.save()


    return render(request, 'index.html',{"msg":msg})


def db(request):

    pass
