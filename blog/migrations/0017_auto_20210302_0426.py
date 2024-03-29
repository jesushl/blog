# Generated by Django 3.1.2 on 2021-03-02 04:26

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20201011_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobexperience',
            name='contact_card',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(blank=True, choices=[('t', 'Technology'), ('h', 'Hobby'), ('b', 'Book'), ('m', 'Movie'), ('p', 'Profile')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=10000, null=True),
        ),
    ]
