# Generated by Django 3.1.14 on 2022-01-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20220127_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Aibler'), (1, 'Tutor')], default=0),
        ),
    ]
