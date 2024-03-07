# Generated by Django 5.0.2 on 2024-03-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sparklabs', '0003_delete_contact_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email_sub', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=100)),
                ('project_desc', models.CharField(max_length=500)),
                ('project_link', models.CharField(default='', max_length=100)),
                ('project_category', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField()),
                ('project_image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
