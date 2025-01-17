# Generated by Django 3.0.4 on 2020-03-31 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gezi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gezi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=30)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('detail', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gezi.Category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='gezi.Gezi')),
            ],
        ),
    ]
