# Generated by Django 3.2.5 on 2022-04-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_user_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('rate_course', 'Rate course'),)},
        ),
    ]
