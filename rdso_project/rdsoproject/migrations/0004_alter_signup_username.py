# Generated by Django 4.2.2 on 2023-06-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdsoproject', '0003_alter_signup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
