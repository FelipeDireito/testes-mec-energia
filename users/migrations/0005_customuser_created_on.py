# Generated by Django 4.1 on 2022-12-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
