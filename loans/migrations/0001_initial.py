# Generated by Django 4.1.5 on 2023-02-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('administration', '0001_initial'),
        ('assetmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.basemodel')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('document_type', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='documents/')),
            ],
            bases=('administration.basemodel',),
        ),
        migrations.CreateModel(
            name='documentType',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.basemodel')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            bases=('administration.basemodel',),
        ),
        migrations.CreateModel(
            name='Loan_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('need_collateral', models.BooleanField(help_text='does this type of Loan need Coollateral')),
                ('need_guarantor', models.BooleanField(help_text='does this type of loan need a gurantor')),
                ('market', models.CharField(choices=[('Enterpreneurs', 'Enterpreneurs'), ('White Collar Jobs', 'White Collar Jobs'), ('Students', 'Student'), ('General', 'General'), ('Others', 'Others')], help_text='these include the category of people who will be interested in this particular product', max_length=50, null=True)),
                ('min_amount_allowed', models.IntegerField(blank=True, null=True)),
                ('max_amount_allowed', models.IntegerField(blank=True, null=True)),
                ('interest_type', models.CharField(choices=[('Flat Rate', 'Flat Rate'), ('Reducing Balance', 'Reducing Balance')], default='Flat Rate', max_length=50)),
                ('documents', models.ManyToManyField(help_text='Include documents that are needed here for this particular loan.. You can go to the document section to add or delete document', to='loans.documenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('submitted', 'submitted'), ('in review', 'in review'), ('Open', 'Open'), ('Closed', 'Closed')], max_length=200)),
                ('application_date', models.DateField(auto_now_add=True)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('repayment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_frequency', models.CharField(choices=[('daily', 'daily'), ('monthly', 'monthly'), ('quaterly', 'quaterly'), ('bi-annual', 'bi-annual'), ('yearly', 'yearly')], max_length=50)),
                ('repaid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('loan_interest', models.DecimalField(decimal_places=2, default=0.012, max_digits=8)),
                ('late_charge', models.IntegerField(default=100)),
                ('collateral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_colateral', to='assetmanager.asset')),
                ('guarantors', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='guarantors', to='members.members')),
                ('lendee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='borrower', to='members.members')),
                ('loan_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loan_type')),
            ],
        ),
    ]