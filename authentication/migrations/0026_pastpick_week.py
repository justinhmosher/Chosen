# Generated by Django 4.1.5 on 2024-02-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0025_remove_pastpick_pick10_remove_pastpick_pick11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastpick',
            name='week',
            field=models.IntegerField(default=1),
        ),
    ]