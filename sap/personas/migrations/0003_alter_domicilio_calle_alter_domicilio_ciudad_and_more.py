# Generated by Django 4.1 on 2022-08-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_domicilio_persona_domicilio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicilio',
            name='calle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='ciudad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
