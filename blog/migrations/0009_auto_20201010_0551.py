# Generated by Django 3.1.2 on 2020-10-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_contactcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcard',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
