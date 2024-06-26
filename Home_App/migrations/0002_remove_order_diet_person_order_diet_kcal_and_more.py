# Generated by Django 5.0.1 on 2024-04-03 20:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_diet',
            name='Person',
        ),
        migrations.AddField(
            model_name='order_diet',
            name='Kcal',
            field=models.CharField(choices=[('option1', '1200 kcal'), ('option2', '1400 kcal'), ('option3', '1500 kcal'), ('option4', '1750 kcal'), ('option5', '1900 kcal'), ('option6', '2150 kcal'), ('option7', '2350 kcal'), ('option8', '2550 kcal'), ('option9', '2700 kcal')], default='option1', max_length=55),
        ),
        migrations.AddField(
            model_name='order_diet',
            name='Variant',
            field=models.CharField(choices=[('option1', 'Allday'), ('option2', 'Family pack'), ('option3', 'Medium'), ('option4', 'Lunch'), ('option5', 'Lunch+'), ('option6', 'Medium+')], default='option1', max_length=55),
        ),
        migrations.AlterField(
            model_name='order_diet',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order_diet',
            name='Number',
            field=models.IntegerField(),
        ),
    ]
