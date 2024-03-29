# Generated by Django 4.2.6 on 2024-01-30 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('fine_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='userfine',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='app.user'),
        ),
        migrations.AlterField(
            model_name='userfine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]
