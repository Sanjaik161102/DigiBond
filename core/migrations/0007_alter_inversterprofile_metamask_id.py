# Generated by Django 3.2.16 on 2022-11-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20221120_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inversterprofile',
            name='metamask_id',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]