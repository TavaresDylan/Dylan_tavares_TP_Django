# Generated by Django 4.1.7 on 2023-02-16 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmo', '0005_alter_movie_duration_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id_director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='filmo.director'),
        ),
    ]
