# Generated by Django 2.1.3 on 2018-11-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20181119_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[('RIG', 'Copyright'), ('CC', 'Creative commons'), ('LEF', 'Copyleft')], max_length=3),
        ),
    ]
