# Generated by Django 4.2.6 on 2024-01-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userfine_created_by_alter_userfine_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfine',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
