# Generated by Django 3.1.2 on 2020-10-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201010_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcard',
            name='adress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactcard',
            name='linkedin',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='contactcard',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactcard',
            name='skype',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactcard',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactcard',
            name='twitter',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
