# Generated by Django 2.2.4 on 2019-08-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0003_code_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='slug',
        ),
        migrations.AddField(
            model_name='code',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]