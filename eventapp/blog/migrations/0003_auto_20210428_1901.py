# Generated by Django 3.2 on 2021-04-28 13:31

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210427_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('IT/Comps Technical', 'IT/Comps Technical'), ('IT/Comps Casual', 'IT/Comps Casual'), ('EXTC', 'EXTC')], default='null', max_length=100),
        ),
    ]