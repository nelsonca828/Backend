# Generated by Django 4.2.6 on 2024-03-23 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DateBook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datebook',
            name='remainingAmount',
        ),
    ]
