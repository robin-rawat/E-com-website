# Generated by Django 3.0.5 on 2020-04-28 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200429_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='decription',
            new_name='description',
        ),
    ]
