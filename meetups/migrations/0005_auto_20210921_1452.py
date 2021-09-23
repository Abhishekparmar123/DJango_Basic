# Generated by Django 3.2.7 on 2021-09-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20210921_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-09-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='org_email',
            field=models.EmailField(default='abhi@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]