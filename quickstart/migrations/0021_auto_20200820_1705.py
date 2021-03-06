# Generated by Django 3.1 on 2020-08-20 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0020_auto_20200820_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_domain_name',
            name='company_Domain_Name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='Company_Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('company_urls', models.URLField(blank=True)),
                ('company_domain_name', models.CharField(blank=True, max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
