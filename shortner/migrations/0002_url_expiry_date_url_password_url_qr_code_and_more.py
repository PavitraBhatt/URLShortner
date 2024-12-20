# Generated by Django 5.1.3 on 2024-11-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(default='80cd187b-1bc2-471c-a6fe-3a2725880d75', max_length=36, unique=True),
        ),
    ]
