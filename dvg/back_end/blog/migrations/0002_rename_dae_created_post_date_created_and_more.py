# Generated by Django 5.0.2 on 2024-04-19 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dae_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='namwe',
            new_name='name',
        ),
    ]