# Generated by Django 3.2.9 on 2021-12-04 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chords', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chord',
            old_name='text',
            new_name='name',
        ),
    ]