# Generated by Django 4.1.5 on 2023-02-02 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_on_branch', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.residentialareas')),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_manager', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_branch', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='baseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationbranch', to='administration.branch')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationcreator', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationupdater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]