# Generated by Django 4.1.7 on 2023-02-16 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmo', '0002_alter_actor_age_alter_director_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='lastaname',
            new_name='lastname',
        ),
    ]
