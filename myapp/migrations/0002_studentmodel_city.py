# Generated by Django 4.0.6 on 2022-09-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='city',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]