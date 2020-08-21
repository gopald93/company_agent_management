from django.urls import path
from quickstart.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('simple_upload/', simple_upload, name='simple_upload'),
    path('index/', index, name='index'),
    path('model_form_upload/', model_form_upload, name='model_form_upload'),
    path('languages_data/', languages_data, name='languages_data'),
    path('google_dialog_flow_integration/', google_dialog_flow_integration, name='google_dialog_flow_integration'),
    path('crud/',  CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/',  CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/',  UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('CreateSelected_User_Data',  CreateSelected_User_Data.as_view(), name='CreateSelected_User_Data'),
    path('CreateSelected_User_Data',  CreateSelected_User_Data.as_view(), name='CreateSelected_User_Data'),
    path('mymodelform/',  mymodelform, name='mymodelform'),
    path('welcome_messages/',  welcome_messages, name='welcome_messages'),
    path('company_url/',  company_url, name='company_url'),
    path('company_domain_name/',  company_domain_name, name='company_domain_name'),
    path('company_configuration/',  company_configuration, name='company_configuration'),
    path('company_domain_details/<str:company_domain_name>',company_domain_details, name='company_domain_details')
       
    ]
  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    