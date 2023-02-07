# Generated by Django 4.1.5 on 2023-02-07 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.basemodel')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('expiry_date', models.DateField(null=True)),
                ('inspection_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('submitted', 'submitted'), ('in review', 'in review'), ('Open', 'Open'), ('Closed', 'Closed')], max_length=20, null=True)),
                ('value', models.IntegerField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.members')),
            ],
            bases=('administration.basemodel',),
        ),
        migrations.CreateModel(
            name='assetDocument',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.basemodel')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('document_name', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(upload_to='assetdocuments/')),
                ('proof_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmanager.asset')),
            ],
            bases=('administration.basemodel',),
        ),
    ]
