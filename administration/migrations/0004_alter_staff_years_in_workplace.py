# Generated by Django 4.1.5 on 2023-02-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_remove_staff_phone_staff_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='years_in_workplace',
            field=models.IntegerField(blank=True),
        ),
    ]