# Generated by Django 4.0.5 on 2022-06-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_portugues_link_arquivo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portugues',
            name='tipo_arquivo2',
            field=models.TextField(blank=True),
        ),
    ]
