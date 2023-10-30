# Generated by Django 4.2.6 on 2023-10-29 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudioClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_time', models.CharField(blank=True, max_length=200, null=True)),
                ('class_name', models.ManyToManyField(blank=True, related_name='studio', to='home.classtype')),
            ],
        ),
    ]
