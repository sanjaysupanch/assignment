# Generated by Django 3.0.7 on 2020-06-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200624_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mid',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]