# Generated by Django 2.0.2 on 2019-03-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0008_auto_20190318_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ufeature',
            name='fbrb',
            field=models.BinaryField(null=True, verbose_name='Frequencies of Broken rotor bar'),
        ),
        migrations.AddField(
            model_name='vfeature',
            name='fbrb',
            field=models.BinaryField(null=True, verbose_name='Frequencies of Broken rotor bar'),
        ),
        migrations.AddField(
            model_name='wfeature',
            name='fbrb',
            field=models.BinaryField(null=True, verbose_name='Frequencies of Broken rotor bar'),
        ),
    ]
