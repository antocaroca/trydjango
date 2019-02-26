# Generated by Django 2.1.5 on 2019-02-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
        migrations.AddField(
            model_name='article',
            name='author_name',
            field=models.CharField(default='author', max_length=200),
            preserve_default=False,
        ),
    ]
