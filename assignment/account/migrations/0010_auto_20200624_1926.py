# Generated by Django 3.0.7 on 2020-06-24 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200624_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='account.Member'),
        ),
    ]