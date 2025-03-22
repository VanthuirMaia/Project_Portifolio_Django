# Generated by Django 5.1.7 on 2025-03-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('tecnologias', models.TextField(help_text='Liste as tecnologias utilizadas separadas por vírgula.')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='projetos/')),
                ('github_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
