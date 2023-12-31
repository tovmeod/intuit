# Generated by Django 4.2.3 on 2023-07-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=9)),
                ('birthYear', models.IntegerField(blank=True, null=True)),
                ('birthMonth', models.IntegerField(blank=True, null=True)),
                ('birthDay', models.IntegerField(blank=True, null=True)),
                ('birthCountry', models.CharField(blank=True, max_length=200, null=True)),
                ('birthState', models.CharField(blank=True, max_length=200, null=True)),
                ('birthCity', models.CharField(blank=True, max_length=200, null=True)),
                ('deathYear', models.IntegerField(blank=True, null=True)),
                ('deathMonth', models.IntegerField(blank=True, null=True)),
                ('deathDay', models.IntegerField(blank=True, null=True)),
                ('deathCountry', models.CharField(blank=True, max_length=200, null=True)),
                ('deathState', models.CharField(blank=True, max_length=200, null=True)),
                ('deathCity', models.CharField(blank=True, max_length=200, null=True)),
                ('nameFirst', models.CharField(blank=True, max_length=200, null=True)),
                ('nameLast', models.CharField(max_length=200)),
                ('nameGiven', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('bats', models.CharField(blank=True, max_length=1, null=True)),
                ('throws', models.CharField(blank=True, max_length=1, null=True)),
                ('debut', models.DateField(blank=True, null=True)),
                ('finalGame', models.DateField(blank=True, null=True)),
                ('retroID', models.CharField(blank=True, max_length=9, null=True)),
                ('bbrefID', models.CharField(blank=True, max_length=9, null=True)),
            ],
            options={
                'ordering': ['playerID'],
            },
        ),
    ]
