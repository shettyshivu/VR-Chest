# Generated by Django 3.2.10 on 2022-11-25 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VR_Chest_App', '0011_review_wholeno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='wholeno',
        ),
    ]
