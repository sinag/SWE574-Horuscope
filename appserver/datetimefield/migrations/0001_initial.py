# Generated by Django 2.1.1 on 2020-06-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateTimeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'datetimefield',
                'verbose_name_plural': 'datetimefields',
            },
        ),
    ]
