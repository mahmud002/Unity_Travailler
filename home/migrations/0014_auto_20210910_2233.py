# Generated by Django 3.2.5 on 2021-09-11 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210910_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='gelary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.event'),
        ),
        migrations.DeleteModel(
            name='EventGelary',
        ),
    ]
