# Generated by Django 4.1.2 on 2022-10-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
