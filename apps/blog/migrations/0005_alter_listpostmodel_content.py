# Generated by Django 5.2.1 on 2025-06-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_listpostmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listpostmodel',
            name='content',
            field=models.TextField(),
        ),
    ]
