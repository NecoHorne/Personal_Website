# Generated by Django 2.1.2 on 2018-10-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Neco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]