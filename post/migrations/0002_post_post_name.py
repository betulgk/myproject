# Generated by Django 2.0.7 on 2018-07-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_name',
            field=models.CharField(default=3, max_length=200),
            preserve_default=False,
        ),
    ]
