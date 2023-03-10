# Generated by Django 4.1.5 on 2023-02-26 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='residential_areas',
            fields=[
                ('area_code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'residential_areas',
            },
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('names', models.CharField(blank=True, max_length=255, null=True)),
                ('mbr_no', models.IntegerField(primary_key=True, serialize=False)),
                ('id_no', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=255, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=255, null=True)),
                ('next_of_kin', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_nos', models.CharField(blank=True, max_length=255, null=True)),
                ('relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='members/passport_photo/')),
                ('residential', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='members.residential_areas')),
            ],
            options={
                'db_table': 'members',
            },
        ),
    ]
