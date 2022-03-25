# Generated by Django 4.0 on 2022-03-22 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_user_type'),
        ('dss', '0005_course_c_assignments_course_c_content_course_c_final_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.TextField(default='Comment...')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dss.course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.customuser')),
            ],
            options={
                'ordering': ['user_comment'],
            },
        ),
    ]
