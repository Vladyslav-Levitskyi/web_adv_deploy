# Generated by Django 5.0.7 on 2024-08-03 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_text_chathistory_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatHistory',
        ),
    ]
