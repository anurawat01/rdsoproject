# Generated by Django 4.2.2 on 2023-06-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdsoproject', '0007_remove_signup_department_remove_signup_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
