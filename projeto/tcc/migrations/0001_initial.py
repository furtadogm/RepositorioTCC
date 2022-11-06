# Generated by Django 3.2.16 on 2022-10-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('modalidade', models.IntegerField(choices=[(0, 'Bacharelado'), (1, 'Licenciatura'), (2, 'Tecnológico')])),
            ],
        ),
        migrations.CreateModel(
            name='TCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='arquivos/%Y/%m/%d/')),
                ('resumo', models.TextField()),
                ('titulo', models.CharField(max_length=250)),
                ('ano_doc', models.IntegerField()),
                ('palavra_chave', models.JSONField(default=list)),
            ],
        ),
    ]
