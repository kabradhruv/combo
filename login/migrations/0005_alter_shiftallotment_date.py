# Generated by Django 4.0.5 on 2022-07-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_shiftallotment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftallotment',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
