# Generated by Django 5.1 on 2024-09-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
