# Generated by Django 3.0.8 on 2020-07-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanservice', '0002_auto_20200728_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('id_receive', models.CharField(max_length=14)),
                ('password_receive', models.CharField(max_length=20)),
            ],
        ),
    ]
