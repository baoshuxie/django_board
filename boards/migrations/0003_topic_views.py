# Generated by Django 2.2.7 on 2019-11-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_post_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
