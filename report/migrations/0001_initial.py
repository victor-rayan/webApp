# Generated by Django 3.1.7 on 2021-04-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleReport', models.CharField(max_length=100, verbose_name='Titulo da denúncia:')),
                ('descriptionReport', models.TextField(verbose_name='Nos conte o que aconteceu:')),
            ],
        ),
    ]