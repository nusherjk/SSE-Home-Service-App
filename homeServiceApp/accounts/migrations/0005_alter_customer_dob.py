# Generated by Django 5.1.1 on 2024-10-24 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customer_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 10, 24, 14, 25, 1, 411650, tzinfo=datetime.timezone.utc)),
        ),
    ]
