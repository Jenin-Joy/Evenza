# Generated by Django 5.1.7 on 2025-03-12 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_tbl_complaint_tbl_feedback_tbl_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_Feedback',
        ),
    ]
