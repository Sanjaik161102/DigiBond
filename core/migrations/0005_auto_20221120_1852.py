# Generated by Django 3.2.16 on 2022-11-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20221117_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='bank_name',
            new_name='metamask_id',
        ),
        migrations.RenameField(
            model_name='inverst',
            old_name='bank_name',
            new_name='metamask_id',
        ),
        migrations.RemoveField(
            model_name='department',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='department',
            name='holder_name',
        ),
        migrations.RemoveField(
            model_name='department',
            name='ifsc',
        ),
        migrations.RemoveField(
            model_name='inverst',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='inverst',
            name='holder_name',
        ),
        migrations.RemoveField(
            model_name='inverst',
            name='ifsc',
        ),
        migrations.RemoveField(
            model_name='inversterprofile',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='inversterprofile',
            name='bank_name',
        ),
        migrations.RemoveField(
            model_name='inversterprofile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='inversterprofile',
            name='holder_name',
        ),
        migrations.RemoveField(
            model_name='inversterprofile',
            name='ifsc',
        ),
        migrations.AddField(
            model_name='inversterprofile',
            name='metamask_id',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]