# Generated by Django 3.0.4 on 2020-05-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200507_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='message',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
