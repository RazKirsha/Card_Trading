# Generated by Django 3.2.4 on 2021-06-07 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20210606_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=400)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=400)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.topics')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
