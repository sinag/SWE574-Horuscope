# Generated by Django 2.1.1 on 2020-06-01 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integerfield', '0001_initial'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integerfield',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property'),
        ),
    ]
