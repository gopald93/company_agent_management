# Generated by Django 3.1 on 2020-08-20 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0024_welcome_messages_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_Details',
            fields=[
                ('bot_id', models.AutoField(primary_key=True, serialize=False)),
                ('icon_type', models.CharField(blank=True, max_length=100)),
                ('position', models.BooleanField(default=False)),
                ('iconIndex', models.IntegerField(blank=True, null=True)),
                ('popup', models.BooleanField(default=False)),
                ('notificationTone', models.CharField(blank=True, max_length=100)),
                ('primaryColor', models.CharField(blank=True, max_length=100)),
                ('secondaryColor', models.CharField(blank=True, max_length=100)),
                ('showPoweredBy', models.BooleanField(default=False)),
                ('collectFeedback', models.BooleanField(default=False)),
                ('botMessageDelayInterval', models.IntegerField(blank=True, null=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.company_configuration')),
            ],
        ),
    ]
