# Generated by Django 4.1.4 on 2022-12-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HiringContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PyContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
    ]
