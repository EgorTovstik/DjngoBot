# Generated by Django 5.0 on 2023-12-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_botuser_tg_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='user_id',
        ),
        migrations.AddField(
            model_name='survey',
            name='tg_ID',
            field=models.TextField(max_length=100, null=True, verbose_name='ID пользователя из телеграмма'),
        ),
    ]
