# Generated by Django 4.1 on 2024-06-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
