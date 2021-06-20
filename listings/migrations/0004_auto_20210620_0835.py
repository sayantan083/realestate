# Generated by Django 3.1.1 on 2021-06-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='bedrooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lead',
            name='keywords',
            field=models.CharField(default='', max_length=200),
        ),
    ]