# Generated by Django 2.2.5 on 2019-09-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('visit', models.IntegerField(blank=True)),
                ('status', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Test_Excel',
            },
        ),
    ]
