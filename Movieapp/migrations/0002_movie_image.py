# Generated by Django 4.0.4 on 2022-06-04 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='movie/'),
        ),
    ]
