# Generated by Django 4.0.4 on 2022-06-04 05:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('b_date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='actor/')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('b_date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='director/')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('r_date', models.DateField(default=django.utils.timezone.now)),
                ('actor', models.ManyToManyField(to='Movieapp.actor')),
                ('director', models.ManyToManyField(to='Movieapp.director')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movieapp.gender'),
        ),
        migrations.AddField(
            model_name='actor',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movieapp.gender'),
        ),
    ]
