# Generated by Django 3.2.8 on 2024-05-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='problem_name',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]