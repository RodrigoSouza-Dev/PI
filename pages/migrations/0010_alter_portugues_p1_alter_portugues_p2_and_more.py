# Generated by Django 4.0.5 on 2022-06-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_portugues_p1_alter_portugues_p2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portugues',
            name='p1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portugues',
            name='p2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portugues',
            name='p3',
            field=models.TextField(blank=True),
        ),
    ]
