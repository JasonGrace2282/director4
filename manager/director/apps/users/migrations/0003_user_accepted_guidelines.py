# Generated by Django 2.2.12 on 2020-04-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_guidelines',
            field=models.BooleanField(default=False),
        ),
    ]