# Generated by Django 4.2.1 on 2023-06-23 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Droga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DrogaPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade_pu', models.IntegerField()),
                ('frequencia', models.CharField(max_length=30)),
                ('ultimo_uso', models.DateField()),
                ('droga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='droga', to='paciente.droga')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='paciente.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='drogas',
            field=models.ManyToManyField(blank=True, through='paciente.DrogaPaciente', to='paciente.droga'),
        ),
    ]
