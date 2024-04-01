# Generated by Django 5.0.3 on 2024-04-01 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prog_name', models.CharField(max_length=100)),
                ('prog_description', models.TextField()),
                ('registration_fees', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RegistersFor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.program')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]