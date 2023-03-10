# Generated by Django 4.1.5 on 2023-02-26 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='globalCharges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('maintenance_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('late_charges', models.DecimalField(decimal_places=2, max_digits=5)),
                ('loan_form', models.DecimalField(decimal_places=2, max_digits=5)),
                ('general_charges', models.DecimalField(decimal_places=2, max_digits=5)),
                ('affidavit_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('passbook', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'global_charges',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_on_branch', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.residential_areas')),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_manager', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_branch', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'branch',
            },
        ),
        migrations.CreateModel(
            name='baseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='administration.branch')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationcreator', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationupdater', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'base_model',
            },
        ),
    ]
