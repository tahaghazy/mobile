# Generated by Django 3.1.1 on 2020-09-19 07:18

import creditcards.models
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('cc_number', creditcards.models.CardNumberField(max_length=25, verbose_name='card number')),
                ('cc_expiry', creditcards.models.CardExpiryField(verbose_name='expiration date')),
                ('cc_code', creditcards.models.SecurityCodeField(max_length=4, verbose_name='security code')),
            ],
        ),
    ]
