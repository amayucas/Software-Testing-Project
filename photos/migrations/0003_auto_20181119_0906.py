# Generated by Django 2.1.3 on 2018-11-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20181119_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[('CC', 'Creative commons'), ('RIG', 'Copyright'), ('LEF', 'Copyleft')], max_length=3),
        ),
    ]
