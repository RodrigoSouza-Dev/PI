# Generated by Django 4.0.5 on 2022-07-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_rename_tipo_arquivo1_portugues_atividades_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portugues',
            name='audio_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='portugues',
            name='nome_conteudo',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]