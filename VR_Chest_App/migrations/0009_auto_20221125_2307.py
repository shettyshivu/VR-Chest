# Generated by Django 3.2.10 on 2022-11-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VR_Chest_App', '0008_alter_gallery_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='half',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]