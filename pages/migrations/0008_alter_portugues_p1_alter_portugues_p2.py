# Generated by Django 4.0.5 on 2022-06-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_rename_resumo_portugues_p1_portugues_p2_portugues_p3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portugues',
            name='p1',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='portugues',
            name='p2',
            field=models.TextField(default=None),
        ),
    ]
