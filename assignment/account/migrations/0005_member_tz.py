# Generated by Django 3.0.7 on 2020-06-24 12:38

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_member_tz'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='tz',
            field=timezone_field.fields.TimeZoneField(default='Europe/London'),
        ),
    ]
