# Generated by Django 3.2.9 on 2021-12-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_jugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosibleJugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
            ],
        ),
    ]
