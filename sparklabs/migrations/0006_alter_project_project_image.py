# Generated by Django 5.0.2 on 2024-03-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparklabs', '0005_alter_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to='static/projects/images'),
        ),
    ]
