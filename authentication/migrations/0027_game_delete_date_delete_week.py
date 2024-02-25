# Generated by Django 4.1.5 on 2024-02-24 02:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0026_pastpick_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(default='type a sport', max_length=100)),
                ('startDate', models.DateField(default=datetime.date.today)),
                ('endDate', models.DateField(default=datetime.date.today)),
                ('pot', models.IntegerField(default=1000)),
                ('week', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='Week',
        ),
    ]