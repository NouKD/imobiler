# Generated by Django 3.1.3 on 2020-11-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sujet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]