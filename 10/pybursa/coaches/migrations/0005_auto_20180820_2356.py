# Generated by Django 2.0.7 on 2018-08-20 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_coache_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coache',
            name='dossier',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coaches.Dossier'),
        ),
    ]