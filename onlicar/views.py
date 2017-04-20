from django.shortcuts import render
from django.http import HttpResponse
from .models import data_table
import json
import datetime
import ast


import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'vehicles.json')
#print file_path
# Create your views here.

class ReadJason:
    def __init__(self, file_name):
        self.file_name=file_name
        self.data=[]
        self.MakeAList()


    def MakeAList(self):
        with open(self.file_name) as json_data:
            d = json.load(json_data)
            #d is a list of dictionaries, right ?
            for entry in d:
                #for each dictionary in the list of dictionary
                driver_name=entry["driver_name"]
                insurance=entry["insurance"]
                tax=entry["tax"]
                mot=entry["mot"]
                phone_no=str(entry["driver_phone"])
                #print (entry["model_data"])

                model_data=ast.literal_eval(entry["model_data"]) #It's a dictioanary but is saved as string ----
                #  this converts to python dictionary..got it ?


                #for key in model_data:
                    #print key
                lastMotDate=model_data["lastMotDate"]
                model_name = model_data["additionalData"]["model"]
                """FORMAT THE DATE as Mar 21, 2017"""
                k = datetime.datetime.strptime(lastMotDate, "%d/%m/%Y").date()
                fmt = '%b %d, %Y'
                lastMotDate= str(k.strftime(fmt))
                if not str(phone_no).startswith("0"):
                    phone_no="0"+phone_no
                self.data.append([driver_name,insurance,tax,mot,phone_no,lastMotDate,model_name])

def index(request):
    # return HttpResponse('Hello from Python!')
    msg=""
    data=[]
    if request.method == "POST": #If YOU WANT TO POPULATE
        msg="Data populated succesfully...."

                #print type(lastMotDate)
        JasonAsList = ReadJason(file_path)
        data=JasonAsList.data
        """for each_model in JasonAsList.data:
            new_obj=data_table(driver_name=each_model[0],insurance=each_model[1],tax=each_model[2],mot=each_model[3],phone_no=each_model[4],lastMotDate=each_model[5],model_name=each_model[6])
            new_obj.save()"""



    return render(request, 'index.html',{"data":data})





def db(request):

    pass
