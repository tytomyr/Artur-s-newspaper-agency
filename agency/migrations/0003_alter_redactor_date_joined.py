# Generated by Django 4.1.7 on 2023-03-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_alter_newspaper_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redactor',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]