# Generated by Django 5.1.1 on 2024-10-24 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customer_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 10, 24, 14, 24, 18, 159514, tzinfo=datetime.timezone.utc)),
        ),
    ]
