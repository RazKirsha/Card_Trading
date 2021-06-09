# Generated by Django 3.2.4 on 2021-06-06 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210606_1511'),
        ('trading', '0004_remove_card_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile'),
        ),
    ]
