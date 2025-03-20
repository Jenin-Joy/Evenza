# Generated by Django 5.1.4 on 2025-03-07 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_packagetype'),
        ('Guest', '0007_alter_tbl_organization_org_place'),
        ('User', '0006_tbl_booking_tbl_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Custombooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Custombooking_date', models.DateField(auto_now_add=True)),
                ('Custombooking_todate', models.DateField(null=True)),
                ('Custombooking_description', models.CharField(max_length=30)),
                ('Custombooking_amount', models.CharField(max_length=30)),
                ('Custombooking_status', models.IntegerField(default=0)),
                ('Packagetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_packagetype')),
                ('Place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
                ('Serviceprovider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_serviceprovider')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
