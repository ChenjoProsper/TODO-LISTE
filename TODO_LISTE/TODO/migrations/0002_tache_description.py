# Generated by Django 3.2.15 on 2024-04-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='description',
            field=models.TextField(default='ras', max_length=500),
            preserve_default=False,
        ),
    ]
