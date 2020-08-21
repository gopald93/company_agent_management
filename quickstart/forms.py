from django import forms
from quickstart.models import Document,ModelWithLanguage,Google_Dialog_Flow_Integration,MyModel,welcome_messages,Company_Urls,Company_Domain_Name,Company_Configuration

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class ModelWithLanguageForm(forms.ModelForm):
    class Meta:
        model = ModelWithLanguage
        fields = ('language',)

class Google_Dialog_Flow_IntegrationForm(forms.ModelForm):
    class Meta:
        model = Google_Dialog_Flow_Integration
        fields = ('dialogflow_knowledge_base_id','default_bot_language_in_dialogflow','Service_account_private_key_file')




class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('my_field',)


class welcome_messagesform(forms.ModelForm):
    class Meta:
        model = welcome_messages
        fields = ('collect_email_id_from_anonymous_users','show_welcome_message_to_users',
        	'default_language','default_welcome_message')   

        labels = {
            "default_language": "embed"
            
        }	     


class Company_UrlsForm(forms.ModelForm):
    class Meta:
        model = Company_Urls
        fields = ('company_urls','company_name')   

class Company_Domain_NameForm(forms.ModelForm):
    class Meta:
        model = Company_Domain_Name 
        fields = ('company_Domain_Name',)
    

class Company_ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Company_Configuration 
        fields = ('company_name','company_urls','company_domain_name',)