# Generated by Django 3.2.4 on 2021-06-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0010_alter_card_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='color',
            field=models.CharField(default='#ffffff', max_length=200),
        ),
        migrations.AddField(
            model_name='card',
            name='type',
            field=models.CharField(default='regular', max_length=200),
        ),
    ]
