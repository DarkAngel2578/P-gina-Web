# Generated by Django 5.0.6 on 2024-05-09 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrimaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='objetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidasfera', models.CharField(max_length=200)),
                ('banda_focus', models.TextField()),
                ('id_pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPrimaria.pokemones')),
            ],
        ),
    ]
