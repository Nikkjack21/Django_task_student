# Generated by Django 4.1.2 on 2022-10-13 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='address',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
