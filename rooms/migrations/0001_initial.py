# Generated by Django 4.0 on 2021-12-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuxSilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100)),
                ('data', models.TextField(blank=True, default=None)),
                ('link', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('time', models.DateTimeField(blank=True, default=None, null=True)),
                ('data_hash', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
