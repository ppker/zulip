# Generated by Django 5.0.9 on 2024-12-18 09:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0647_alter_stream_can_send_message_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stream",
            name="stream_post_policy",
        ),
    ]