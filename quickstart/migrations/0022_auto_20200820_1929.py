# Generated by Django 3.1 on 2020-08-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0021_auto_20200820_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_configuration',
            name='id',
        ),
        migrations.AddField(
            model_name='company_configuration',
            name='cid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]