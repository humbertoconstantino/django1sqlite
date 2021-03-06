# Generated by Django 2.2.15 on 2021-04-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='sobrenome')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
            ],
        ),
    ]
