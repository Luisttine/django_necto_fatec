# Generated by Django 3.2.5 on 2021-07-27 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('texto', models.TextField(verbose_name='Corpo')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('data_pub', models.DateTimeField(verbose_name='Publicado em')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
