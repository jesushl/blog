# Generated by Django 3.1.2 on 2020-10-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.CharField(choices=[('eng', 'english'), ('esp', 'español')], default='esp', max_length=3),
        ),
    ]