# Generated by Django 5.0.6 on 2024-06-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticky_notes', '0003_stickynote_delete_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickynote',
            name='color',
            field=models.CharField(default='#ffff00', max_length=20),
        ),
    ]
