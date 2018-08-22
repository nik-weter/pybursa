# Generated by Django 2.0.7 on 2018-08-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180807_1323'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(choices=[('s', 'Standard'), ('g', 'Gold'), ('p', 'Platinum')], default='s', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]