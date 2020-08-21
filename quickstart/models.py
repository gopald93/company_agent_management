from django.db import models
import uuid
import pytz
from django.conf.global_settings import LANGUAGES
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

def create_time_zone():
    main_time_zone_list=[]
    for tz in pytz.all_timezones:
        demo_data=(tz,tz)
        main_time_zone_list.append(demo_data)
    return  main_time_zone_list   

class Employee(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=20, null=True, blank=True)
    tz = models.CharField(max_length=1000,choices=create_time_zone(),default="Asia/Kolkata",null=True, blank=True)
    def __str__(self):
       return self.real_name

class Activity_Periods(models.Model):       
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)   
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
       return str(self.start_date)+"To"+str(self.end_date)

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)
    def __str__(self):
        return self.name

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)        


class ModelWithLanguage(models.Model):
    language = models.CharField(max_length=7, choices=LANGUAGES)




class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

class DemoUser(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)



class Selected_User_Data(models.Model):
    selected_name = models.CharField(max_length=30, blank=True)
    selected_address = models.CharField(max_length=100, blank=True)
    selected_age = models.IntegerField(blank=True, null=True)




class Work_Experience(models.Model):
    job_title       = models.CharField(max_length=100, null=True, blank=True)
    company         = models.CharField(max_length=100, null=True, blank=True)
    description     = models.CharField(max_length=300, null=True, blank=True)
    exp_start_date  = models.DateField(null=True, blank=True)
    exp_end_date    = models.DateField(null=True, blank=True)
    is_working      = models.BooleanField(default=False)    

MY_CHOICES = (('krishna', 'krishna'),
              ('gopal', 'gopal'),
              ('dubey', 'dubey'),
              ('ashutosh', 'ashutosh'),
              ('avinash', 'avinash'))

MY_CHOICES2 = ((1, 'Item title 2.1'),
               (2, 'Item title 2.2'),
               (3, 'Item title 2.3'),
               (4, 'Item title 2.4'),
               (5, 'Item title 2.5'))


class MyModel(models.Model):
    my_field = MultiSelectField(choices=MY_CHOICES)
    my_field2 = MultiSelectField(choices=MY_CHOICES2,
                                 max_choices=10,
                                 max_length=10)


LANGUAGE_CHOICES = (("English","English"),
              ("Mandarin Chinese", "Mandarin Chinese"),
              ("Hindi", "Hindi"),
              ("Spanish", "Spanish"),
              ("Arabic", "Arabic"),
              ("Bangla", "Bangla"),
              ("Russian", "Russian"),
              ("Portuguese", "Portuguese"),
              ("Indonesian", "Indonesian"),
              ("Urdu", "Urdu"),)


# class Company_Profile(models.Model):
#     company_name = models.CharField(max_length=30, blank=True)
#     company_url = models.CharField(max_length=100, blank=True)

class Company_Urls(models.Model):
    company_name = models.CharField(max_length=30,unique=True)
    company_urls=models.URLField(max_length = 200,unique=True)
    
class Company_Domain_Name(models.Model): 
    company_Domain_Name=models.CharField(max_length=30,blank=False,unique=True)
#####################






class Company_Configuration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cid = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100,blank=True)
    company_urls=models.URLField(max_length = 200,blank=True)
    company_domain_name=models.CharField(max_length=300,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name


class welcome_messages(models.Model):
    cid = models.ForeignKey(Company_Configuration, on_delete=models.CASCADE)
    collect_email_id_from_anonymous_users = models.BooleanField(null=True, blank=True,default=False)
    show_welcome_message_to_users=models.BooleanField(null=True, blank=True,default=False)
    default_language=MultiSelectField(choices=LANGUAGE_CHOICES)
    default_welcome_message = models.TextField(blank=True)



class Bot_Details(models.Model):
    bot_id= models.AutoField(primary_key=True)
    cid = models.ForeignKey(Company_Configuration,on_delete=models.CASCADE)
    icon_type= models.CharField(max_length=100,blank=True)
    position= models.BooleanField(default=False)
    iconIndex=models.IntegerField(blank=True,null=True)
    popup=models.BooleanField(default=False)
    notificationTone= models.CharField(max_length=100,blank=True)
    primaryColor= models.CharField(max_length=100,blank=True)
    secondaryColor=models.CharField(max_length=100,blank=True)
    showPoweredBy=models.BooleanField(default=False)
    collectFeedback=models.BooleanField(default=False)
    botMessageDelayInterval=models.IntegerField(blank=True,null=True)

class Google_Dialog_Flow_Integration(models.Model):
    bot_id=models.ForeignKey(Bot_Details,on_delete=models.CASCADE)
    dialogflow_knowledge_base_id = models.CharField(max_length=255)
    default_bot_language_in_dialogflow=models.CharField(max_length=100, choices=LANGUAGES)
    Service_account_private_key_file=models.FileField(upload_to='documents/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.dialogflow_knowledge_base_id

