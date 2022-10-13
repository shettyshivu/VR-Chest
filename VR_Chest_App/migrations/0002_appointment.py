# Generated by Django 3.2.10 on 2022-10-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VR_Chest_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Mobileno', models.BigIntegerField()),
                ('Email', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Doctor', models.CharField(max_length=30)),
            ],
        ),
    ]
