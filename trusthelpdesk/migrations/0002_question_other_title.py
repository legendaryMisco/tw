# Generated by Django 3.1.14 on 2023-02-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trusthelpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='other_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
