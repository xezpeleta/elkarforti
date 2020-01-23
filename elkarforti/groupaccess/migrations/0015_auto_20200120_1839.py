# Generated by Django 3.0.2 on 2020-01-20 18:35

from django.db import migrations
import os

class Migration(migrations.Migration):

    dependencies = [
        ('groupaccess', '0014_fortiparameters_fortikeystorepath'),
    ]


    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME', "default")
        DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME','admin')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL','admin@example.com')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD','admin')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]


