# Generated by Django 3.2.8 on 2024-05-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0003_submission_problem_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=50, unique=True)),
                ('std', models.CharField(max_length=10000)),
            ],
        ),
    ]