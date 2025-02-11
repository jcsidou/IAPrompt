# Generated by Django 5.0.7 on 2024-07-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='prompt',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='core.categoria'),
        ),
    ]
