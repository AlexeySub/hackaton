# Generated by Django 2.1.7 on 2019-10-29 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='addDateTime',
            field=models.DateTimeField(auto_now_add=True, db_column='addDateTime', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='updateDateTime',
            field=models.DateTimeField(auto_now=True, db_column='updateDateTime'),
        ),
    ]
