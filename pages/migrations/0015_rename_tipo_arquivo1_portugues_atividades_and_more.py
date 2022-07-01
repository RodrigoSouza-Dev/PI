# Generated by Django 4.0.5 on 2022-07-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_portugues_link_arquivo2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portugues',
            old_name='tipo_arquivo1',
            new_name='atividades',
        ),
        migrations.RenameField(
            model_name='portugues',
            old_name='link_arquivo2',
            new_name='id_video',
        ),
        migrations.RenameField(
            model_name='portugues',
            old_name='tipo_arquivo3',
            new_name='nome_arquivo1',
        ),
        migrations.RenameField(
            model_name='portugues',
            old_name='tipo_arquivo2',
            new_name='nome_arquivo2',
        ),
        migrations.AddField(
            model_name='habilidades',
            name='p1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='habilidades',
            name='p2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='habilidades',
            name='p3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lembrete',
            name='assunto',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lembrete',
            name='p1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='matematica',
            name='atividades',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='matematica',
            name='id_video',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='matematica',
            name='link_arquivo1',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='matematica',
            name='link_arquivo3',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='matematica',
            name='nome_arquivo1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='matematica',
            name='nome_arquivo2',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='matematica',
            name='p1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='matematica',
            name='p2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='matematica',
            name='p3',
            field=models.TextField(blank=True),
        ),
    ]