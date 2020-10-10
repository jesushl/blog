# Generated by Django 3.1.2 on 2020-10-10 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_contactcard_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactcard',
            name='experience',
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='contact_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.contactcard'),
        ),
    ]
