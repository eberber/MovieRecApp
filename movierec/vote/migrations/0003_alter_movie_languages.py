# Generated by Django 4.2.9 on 2024-02-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_movie_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='languages',
            field=models.CharField(choices=[('Dutch', 'DUTCH'), ('English', 'ENGLISH'), ('German', 'GERMAN'), ('Japanese', 'JAPANESE'), ('Spanish', 'SPANISH')], default='English', max_length=50),
        ),
    ]
