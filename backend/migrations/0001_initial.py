# Generated by Django 2.1.7 on 2019-10-29 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('description', models.CharField(db_column='description', max_length=255)),
                ('deadline', models.DateTimeField(db_column='deadline')),
                ('status', models.BooleanField(db_column='status', default=False)),
                ('longitude', models.FloatField(db_column='longitude')),
                ('latitude', models.FloatField(db_column='latitude')),
            ],
            options={
                'db_table': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('firstName', models.CharField(db_column='firstName', max_length=255)),
                ('patronymic', models.CharField(db_column='patronymic', max_length=255)),
                ('lastName', models.CharField(db_column='lastName', max_length=255)),
                ('phone', models.IntegerField(db_column='phone', max_length=11, unique=True)),
            ],
            options={
                'db_table': 'Workers',
            },
        ),
        migrations.AddField(
            model_name='tasks',
            name='id_worker',
            field=models.ForeignKey(db_column='idWorker', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.Workers'),
        ),
    ]
