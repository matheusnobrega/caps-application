# Generated by Django 4.2.1 on 2023-06-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0001_initial'),
        ('paciente', '0002_droga_drogapaciente_paciente_drogas'),
    ]

    operations = [
        migrations.AddField(
            model_name='evolucao',
            name='servidor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='servidores', to='servidor.servidor'),
            preserve_default=False,
        ),
    ]
