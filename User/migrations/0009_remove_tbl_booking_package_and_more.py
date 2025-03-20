# Generated by Django 5.1.4 on 2025-03-07 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_packagetype'),
        ('User', '0008_remove_tbl_booking_packagetype_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_booking',
            name='package',
        ),
        migrations.AddField(
            model_name='tbl_booking',
            name='Packagetype_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_packagetype'),
        ),
    ]
