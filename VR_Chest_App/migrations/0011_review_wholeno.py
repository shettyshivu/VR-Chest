# Generated by Django 3.2.10 on 2022-11-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VR_Chest_App', '0010_alter_review_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='wholeno',
            field=models.IntegerField(default=4),
        ),
    ]
