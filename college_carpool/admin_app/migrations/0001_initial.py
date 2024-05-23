# Generated by Django 5.1 on 2024-05-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(auto_now_add=True)),
                ('total_trips', models.IntegerField()),
                ('total_users', models.IntegerField()),
            ],
        ),
    ]