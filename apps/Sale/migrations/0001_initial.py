# Generated by Django 4.2.6 on 2024-03-23 14:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DateBook', '0001_initial'),
        ('Medicine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('saleDate', models.DateField(default=django.utils.timezone.now)),
                ('profit', models.FloatField(blank=True, default=0, editable=False, null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='DateBook.datebook')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicine.medicine')),
            ],
        ),
    ]
