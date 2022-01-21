# Generated by Django 3.2.11 on 2022-01-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20220121_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='students',
            field=models.ManyToManyField(related_name='students', to='student.Teacher'),
        ),
    ]
