# Generated by Django 3.2 on 2021-04-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_limit', models.PositiveIntegerField(default=10)),
                ('blog_limit', models.PositiveIntegerField(default=10)),
            ],
        ),
    ]
