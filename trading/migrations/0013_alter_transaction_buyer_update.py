# Generated by Django 3.2.4 on 2021-06-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0012_transaction_buyer_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='buyer_update',
            field=models.CharField(default='n', max_length=100),
        ),
    ]
