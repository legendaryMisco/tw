# Generated by Django 3.1.14 on 2023-02-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trusthelpdesk', '0002_question_other_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.TextField(),
        ),
    ]
