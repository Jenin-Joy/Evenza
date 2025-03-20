# Generated by Django 5.1.4 on 2025-03-07 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serviceprovider', '0002_tbl_work_tbl_gallery'),
        ('User', '0007_tbl_custombooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='Packagetype_id',
        ),
        migrations.AddField(
            model_name='tbl_booking',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Serviceprovider.tbl_addpackage'),
        ),
    ]
