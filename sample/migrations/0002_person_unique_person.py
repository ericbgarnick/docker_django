# Generated by Django 3.2.8 on 2021-10-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('name', 'age'), name='unique_person'),
        ),
    ]
