# Generated by Django 3.2.5 on 2021-08-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210821_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='title',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]
