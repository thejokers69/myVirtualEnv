# Generated by Django 5.0.3 on 2024-04-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_description', models.TextField()),
                ('class_hours', models.IntegerField()),
            ],
        ),
    ]
