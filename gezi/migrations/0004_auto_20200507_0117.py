# Generated by Django 3.0.4 on 2020-05-06 22:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gezi', '0003_auto_20200331_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gezi',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]