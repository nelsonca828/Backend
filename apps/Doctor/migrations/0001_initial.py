# Generated by Django 5.0.3 on 2024-03-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameDoctor', models.CharField(max_length=30)),
                ('lastNames', models.CharField(max_length=100)),
                ('folioDoctor', models.IntegerField(default=0, unique=True)),
            ],
        ),
    ]
