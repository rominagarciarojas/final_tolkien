# Generated by Django 4.0.4 on 2022-05-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_profesor_remove_persona_cargo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=100)),
                ('curso', models.IntegerField()),
                ('docente', models.CharField(max_length=100)),
                ('modalidad', models.CharField(max_length=100)),
            ],
        ),
    ]
