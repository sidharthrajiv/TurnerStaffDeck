# Generated by Django 2.0.13 on 2019-03-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reviews', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reviews', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reviews', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Self',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reviews', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='View',
        ),
    ]
