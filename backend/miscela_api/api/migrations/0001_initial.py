# Generated by Django 2.2 on 2019-12-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.CharField(max_length=100)),
                ('maxAtt', models.IntegerField()),
                ('minSup', models.IntegerField()),
                ('evoRate', models.FloatField()),
                ('distance', models.FloatField()),
                ('json_output', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CapCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.CharField(max_length=100)),
                ('maxAtt', models.IntegerField()),
                ('minSup', models.IntegerField()),
                ('evoRate', models.FloatField()),
                ('distance', models.FloatField()),
                ('sensors', models.TextField()),
                ('indexes', models.TextField()),
                ('attributes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.TextField()),
                ('data_type', models.TextField()),
                ('data_id', models.IntegerField()),
                ('data', models.TextField()),
            ],
        ),
    ]
