# Generated by Django 4.1.5 on 2023-02-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0010_alter_loans_issue_date_alter_loans_repayment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='application_date',
            field=models.DateField(),
        ),
    ]