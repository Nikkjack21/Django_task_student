# Generated by Django 4.1.2 on 2022-10-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]