# Generated by Django 4.0 on 2022-03-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0002_alter_course_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='c_department',
            field=models.CharField(default='empty', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='c_id',
            field=models.CharField(default='empty', max_length=100),
            preserve_default=False,
        ),
    ]
