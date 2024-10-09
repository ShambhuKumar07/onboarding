# Generated by Django 3.2 on 2021-04-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_due',
            field=models.CharField(choices=[('AI', 'Info'), ('AS', 'After Signing'), ('PR', 'Preparation'), ('BF', 'Before Work Start'), ('FR', 'First Day of Work'), ('AF', 'After First Day of Work')], default='BF', max_length=2),
        ),
    ]