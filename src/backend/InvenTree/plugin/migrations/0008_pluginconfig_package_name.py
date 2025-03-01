# Generated by Django 3.2.23 on 2024-02-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugin', '0007_auto_20230805_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='pluginconfig',
            name='package_name',
            field=models.CharField(blank=True, help_text='Name of the installed package, if the plugin was installed via PIP', max_length=255, null=True, verbose_name='Package Name'),
        ),
    ]
