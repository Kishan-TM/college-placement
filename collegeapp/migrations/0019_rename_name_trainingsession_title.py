# Generated by Django 5.1.3 on 2024-12-02 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0018_trainingsession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainingsession',
            old_name='name',
            new_name='title',
        ),
    ]
