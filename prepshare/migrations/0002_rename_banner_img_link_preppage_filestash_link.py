# Generated by Django 3.2.3 on 2021-07-01 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prepshare', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preppage',
            old_name='banner_img_link',
            new_name='filestash_link',
        ),
    ]