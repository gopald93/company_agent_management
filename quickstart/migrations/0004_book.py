# Generated by Django 3.0.4 on 2020-03-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20200331_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_number', models.CharField(max_length=13)),
            ],
        ),
    ]