# Generated by Django 5.0.3 on 2024-04-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', upload_to='private/resumes'),
        ),
    ]
