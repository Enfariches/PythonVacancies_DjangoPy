# Generated by Django 4.1.5 on 2023-01-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='dict',
            name='title',
            field=models.CharField(default='default title', max_length=255),
        ),
    ]
