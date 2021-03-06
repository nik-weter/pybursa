# Generated by Django 2.0.7 on 2018-08-07 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_assistent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_assistant', to='coaches.Coache'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prepod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coaches.Coache'),
        ),
    ]
