# Generated by Django 3.2 on 2022-09-02 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_guest_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
    ]
