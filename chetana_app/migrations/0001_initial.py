# Generated by Django 3.1.1 on 2022-01-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.TextField(help_text='Event id should be unique. use the following formate - eventnameyear for example parichaya2021. Please note no space should be given in between.', max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField(help_text='Upload the image to Cloudinary website and generate a link and paste it here.')),
                ('summary', models.TextField()),
                ('teamsize', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('winner_object', models.BooleanField(help_text='Please keep it checked if there is any winner. if there are no winners keep it unchecked and write any random values in winner and runner fields')),
                ('winner', models.TextField(help_text='Please mention name, year and branch. If there are multiple people use <br> tag to separate each winner.')),
                ('runner', models.TextField(help_text='Please mention name, year and branch. If there are multiple people use <br> tag to separate each runner.')),
                ('participants', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Upcoming_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_object', models.BooleanField(help_text='Please keep it checked if there is any upcoming event and uncheck it after completion of the event.')),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField(help_text='Upload the image to Cloudinary website and generate a link and paste it here.')),
                ('reglink', models.TextField()),
                ('description', models.TextField()),
                ('teamsize', models.CharField(max_length=100)),
                ('dates', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('name1', models.CharField(help_text='Name1 mentioned in Poster', max_length=100)),
                ('name2', models.CharField(help_text='Name2 mentioned in Poster', max_length=100)),
                ('contact1', models.CharField(help_text='Please maintain the formate - +91 00000 00000', max_length=100)),
                ('contact2', models.CharField(help_text='Please maintain the formate - +91 00000 00000', max_length=100)),
            ],
        ),
    ]
