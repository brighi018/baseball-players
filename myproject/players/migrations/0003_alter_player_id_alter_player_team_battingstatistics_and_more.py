# Generated by Django 5.1.6 on 2025-02-24 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_rename_name_first_player_name_last'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='players.team'),
        ),
        migrations.CreateModel(
            name='BattingStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('games', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.team')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('year', 'player', 'team'), name='unique_batting_stat')],
            },
        ),
        migrations.CreateModel(
            name='PitchingStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('games', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.team')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('year', 'player', 'team'), name='unique_pitching_stat')],
            },
        ),
    ]
