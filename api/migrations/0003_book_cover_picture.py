# Generated by Django 4.1.5 on 2023-02-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_renewal_library_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_picture',
            field=models.TextField(blank=True, null=True),
        ),
    ]
