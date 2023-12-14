# Generated by Django 4.1.5 on 2023-12-14 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_pick_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='isin',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pick',
            name='pick1',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='pick',
            name='pick2',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='pick',
            name='week',
            field=models.IntegerField(default=1),
        ),
    ]
