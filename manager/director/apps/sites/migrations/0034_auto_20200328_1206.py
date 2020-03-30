# Generated by Django 2.2.10 on 2020-03-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0033_auto_20200306_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='DockerImageSetupCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="A short name describing what the command does. If the command is OS/language-specific, please use prefixes like this for consistency:'[OS:Alpine] Fix timezone setup', '[Lang:Python] Install virtualenv with Pip'", max_length=32)),
                ('command', models.TextField(help_text="The command to run. Everything will be '&&'-ed together, so be careful about syntax errors.")),
                ('order', models.IntegerField(help_text='This will be used to sort the setup commands (in ascending order). The following values are recommended for standardization: 0=OS-specific commands, 1=language-specific commands; other values as required for specific use cases.')),
            ],
        ),
        migrations.AlterField(
            model_name='domain',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('deleted', 'Deleted'), ('blocked', 'Blocked')], default='active', max_length=8),
        ),
        migrations.AddField(
            model_name='dockerimage',
            name='setup_commands',
            field=models.ManyToManyField(blank=True, related_name='docker_images', to='sites.DockerImageSetupCommand'),
        ),
    ]