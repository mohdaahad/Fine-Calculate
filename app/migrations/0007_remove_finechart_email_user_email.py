# Generated by Django 4.2.6 on 2024-01-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_finechart_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finechart',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
