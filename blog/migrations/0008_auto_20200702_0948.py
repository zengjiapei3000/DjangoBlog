# Generated by Django 2.2.3 on 2020-07-02 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200702_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tag',
        ),
    ]
