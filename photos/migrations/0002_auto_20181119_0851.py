# Generated by Django 2.1.3 on 2018-11-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[('LEF', 'Copyleft'), ('RIG', 'Copyright'), ('CC', 'Creative commons')], max_length=3),
        ),
    ]
