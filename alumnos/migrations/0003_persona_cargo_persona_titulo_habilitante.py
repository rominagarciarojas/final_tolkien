# Generated by Django 4.0.4 on 2022-05-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alter_persona_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='cargo',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='persona',
            name='titulo_habilitante',
            field=models.CharField(default='', max_length=100),
        ),
    ]
