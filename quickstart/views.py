from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from quickstart.models import *
from django.shortcuts import render, redirect
import csv
import pendulum
from datetime import datetime 
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from quickstart.forms import DocumentForm,ModelWithLanguageForm,Google_Dialog_Flow_IntegrationForm,MyModelForm,welcome_messagesform,Company_UrlsForm,Company_Domain_NameForm,Company_ConfigurationForm
from django.conf.global_settings import LANGUAGES
from django.views.generic import ListView
from .models import CrudUser,DemoUser,Selected_User_Data,Work_Experience
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def change_date_format(date_time_obj):
    required_data_obj = date_time_obj.strftime("%b %d %Y %I%p")
    return required_data_obj

@api_view(['GET'])
def activity_periods_api(request):
    return_dict={}
    return_dict.update({"ok":True})
    return_dict.update({"members":[]})
    if request.method == 'GET': 
        employee_obj = Employee.objects.all()
        for data in employee_obj:
            demo_dict={}
            demo_dict.update({"id":data.id})
            demo_dict.update({"real_name":data.real_name})
            demo_dict.update({"tz":data.tz})
            demo_dict.update({"activity_periods":[]})
            for da in data.activity_periods_set.all():
                demo_dict_temp={}
                date_time_obj=change_date_format(da.start_date)
                demo_dict_temp.update({"start_date":date_time_obj})
                date_time_obj=change_date_format(da.end_date)
                demo_dict_temp.update({"end_date":date_time_obj}) 
                demo_dict.get("activity_periods").append(demo_dict_temp)
            return_dict.get("members").append(demo_dict)
        return Response(return_dict)   
    return Response({"message": "Hello, world!"})

def get_time_zone():
    datetime_object = datetime.now()
    tz_type=pendulum.local(int(datetime_object.year),int(datetime_object.month),int(datetime_object.day))
    local_tz_name=tz_type.timezone.name
    print(local_tz_name)
    return local_tz_name

def create_employee_data(id,real_name,local_tz_name):
    emp_obj,emp_created=Employee.objects.get_or_create(id=id,real_name=real_name,tz=local_tz_name)
    return emp_obj,emp_created


def create_activity_periods(emp_obj,start_date,end_date):
    activity_period_obj,act_per_created=Activity_Periods.objects.get_or_create(employee=emp_obj,start_date=start_date,end_date=end_date)
    return activity_period_obj,act_per_created

def upload_csv(request):
    data={}
    local_tz_name=get_time_zone()
    if "GET" == request.method:
        return render(request, "quickstart/create_normal.html", data)
    else:    
        file = request.FILES["csv_file"] 
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        check_id_available_list=[]
        for row in reader:
            if row.get("id") not in check_id_available_list:
                check_id_available_list.append(row.get("id"))
                emp_obj,created=create_employee_data(row.get("id"),row.get("real_name"),local_tz_name)
            start_time_obj = datetime.strptime(row.get("start_time"), '%Y/%m/%d %H:%M:%S')
            end_time_obj = datetime.strptime(row.get("end_time"), '%Y/%m/%d %H:%M:%S')
            activity_period_obj,act_per_created=create_activity_periods(emp_obj,start_time_obj,end_time_obj)
    return HttpResponse("Successfully upload the file")





def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'quickstart/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'quickstart/simple_upload.html')    



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'quickstart/model_form_upload.html', {
        'form': form
    })



def languages_data(request):
    if request.method == 'POST':
        form = ModelWithLanguageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ModelWithLanguageForm()
    return render(request, 'quickstart/ModelWithLanguage.html', {
        'form': form
    })    


def google_dialog_flow_integration(request):
    if request.method == 'POST':
        form = Google_Dialog_Flow_IntegrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Google_Dialog_Flow_IntegrationForm()
    return render(request, 'quickstart/google_dialog_flow_integration.html', {
        'form': form
    })  



class CrudView(ListView):
    model = CrudUser
    template_name = 'quickstart/crud.html'
    context_object_name = 'users'    

class CreateCrudUser(View):
    def  get(self, request):
        print("=============================================================================>")
        crud_obj=DemoUser.objects.all()


        print(crud_obj.count())
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = DemoUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)   

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class CreateDemoUser(View):
    def  get(self, request):
        print("=============================================================================>")
        crud_obj=DemoUser.objects.all()


        print(crud_obj.count())
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        print(name1)
        print(address1)
        print(age1)
        obj = DemoUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)        


class CreateSelected_User_Data(View):
    def  get(self, request):
        print("=============================================================================>")
        crud_obj=Selected_User_Data.objects.all()
        print(crud_obj.count())
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        print(name1)
        print(address1)
        print(age1)
        obj = Selected_User_Data.objects.create(
            selected_name = name1,
            selected_address = address1,
            selected_age = age1
        )

        user = {'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)                     




def mymodelform(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyModelForm()
    return render(request, 'quickstart/multiple.html', {
        'form': form
    })    


    

def company_url(request):
    if request.method == 'POST':
        form = Company_UrlsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Company_UrlsForm()
    return render(request, 'quickstart/company_url.html', {
        'form': form
    })    


def company_domain_name(request):
    if request.method == 'POST':
        form = Company_Domain_NameForm(request.POST)
        if form.is_valid():
            company_Domain_Name= form.cleaned_data.get("company_Domain_Name")
            form.save()
            return redirect('company_domain_details',company_domain_name=company_Domain_Name)
    else:
        form = Company_Domain_NameForm()
    return render(request, 'quickstart/company_domain.html', {
        'form': form
    })        

  
def company_domain_details(request,company_domain_name):
    print("company_domain_name======>",company_domain_name)
    
    context={}
    return render(request, "quickstart/company_domain_details.html",context)  


def company_configuration(request):
    user_obj = get_object_or_404(User,pk=1)
    if request.method == "POST":
        form = Company_ConfigurationForm(request.POST)
        if form.is_valid():
            company_configuration_obj = form.save(commit=False)
            company_configuration_obj.user = user_obj
            company_configuration_obj.save()
            return redirect('index')
    else:
        form = Company_ConfigurationForm()
    return render(request, "quickstart/company_configuration.html", {'form': form})

def welcome_messages(request):
    company_configuration_obj = get_object_or_404(Company_Configuration,pk=2)
    print(company_configuration_obj)
    if request.method == "POST":
        form = welcome_messagesform(request.POST)
        if form.is_valid():
            welcome_messages_obj = form.save(commit=False)
            welcome_messages_obj.cid = company_configuration_obj
            welcome_messages_obj.save()
            return redirect('index')
    else:
        form = welcome_messagesform()
    return render(request, 'quickstart/welcome_messages.html', {'form': form})


# def google_dialog_flow_integration(request):
#     # company_configuration_obj = get_object_or_404(Bot_Details,pk=2)
    
#     if request.method == 'POST':
#         form = Google_Dialog_Flow_IntegrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = Google_Dialog_Flow_IntegrationForm()
#     return render(request, 'quickstart/google_dialog_flow_integration.html', {
#         'form': form
#     })  


def google_dialog_flow_integration(request):
    bot_details_obj = get_object_or_404(Bot_Details,pk=1)
    print("bot_details_obj========================================>",bot_details_obj)
    print("bot_details_obj====>",bot_details_obj)
    if request.method == "POST":
        form = Google_Dialog_Flow_IntegrationForm(request.POST)
        if form.is_valid():
            google_dialog_flow_integration_obj = form.save(commit=False)
            google_dialog_flow_integration_obj.bid= bot_details_obj
            google_dialog_flow_integration_obj.save()
            return redirect('index')
    else:
        form = Google_Dialog_Flow_IntegrationForm()
    return render(request, 'quickstart/google_dialog_flow_integration.html', {'form': form})





# def welcome_messages(request):
#     if request.method == 'POST':
#         form = welcome_messagesform(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = welcome_messagesform()
#     return render(request, 'quickstart/welcome_messages.html', {
#         'form': form
#     })    
