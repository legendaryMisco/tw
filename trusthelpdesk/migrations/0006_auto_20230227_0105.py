# Generated by Django 3.1.14 on 2023-02-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trusthelpdesk', '0005_auto_20230227_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersinfo',
            options={'verbose_name_plural': 'Users Info'},
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='full_information_issue',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='issues',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='more_issue',
            field=models.TextField(null=True),
        ),
    ]