# Generated by Django 4.1.7 on 2023-05-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_alter_newspaper_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redactor',
            name='years_of_experience',
            field=models.IntegerField(null=True),
        ),
    ]
