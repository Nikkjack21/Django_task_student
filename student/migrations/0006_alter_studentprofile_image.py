# Generated by Django 4.1.2 on 2022-10-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studentprofile_address_studentprofile_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(max_length=2500, null=True, upload_to=''),
        ),
    ]
