# Generated by Django 3.1.2 on 2020-10-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201010_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactcard',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
