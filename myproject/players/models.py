from django.db import models
from asgiref.sync import sync_to_async
import asyncio
from django.shortcuts import get_object_or_404

# Create your models here.

class Team(models.Model):
    org_abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.org_abbreviation

    def get_team_players(self):
        return Player.objects.filter(team=self).order_by('name_last', 'name_use')

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name_first = models.CharField(max_length=100)
    name_use = models.CharField(max_length=100)
    name_last = models.CharField(max_length=100)
    team = models.ForeignKey(Team, null=True, on_delete=models.PROTECT)
    birth_date = models.DateField(null=True)
    height_feet = models.IntegerField(null=True)
    height_inches = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    throws = models.CharField(max_length=1, null=True)
    bats = models.CharField(max_length=1, null=True)
    primary_position = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.name_last + ', ' + self.name_use

    # @classmethod
    # async def get_batting_statistics(self, player_id):
    #     player = get_object_or_404(Player, pk=player_id)
    #     # return await BattingStatistics.objects.filter(player=player)
    #     return await sync_to_async(BattingStatistics.objects.filter(player=player))
    def get_batting_statistics(self):
        return BattingStatistics.objects.filter(player=self).order_by('-year')

    # todo: make async
    def get_pitching_statistics(self):
        return PitchingStatistics.objects.filter(player=self).order_by('-year')

class BattingStatistics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    year = models.IntegerField() # todo: default 0?
    league = models.CharField(max_length=5, null=True)
    org_abbreviation = models.CharField(max_length=5)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    plate_appearances = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    games_started = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    bases_on_balls = models.IntegerField(default=0)
    strikeouts = models.IntegerField(default=0)
    sacrifices = models.IntegerField(default=0)
    sacrifice_flies = models.IntegerField(default=0)
    stolen_bases = models.IntegerField(default=0)
    caught_stealing = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['year', 'player', 'team'], name="unique_batting_stat")
        ]

class PitchingStatistics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    year = models.IntegerField() # todo: default 0?
    league = models.CharField(max_length=5, null=True)
    org_abbreviation = models.CharField(max_length=5)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    games = models.IntegerField(default=0)
    games_started = models.IntegerField(default=0)
    complete_games = models.IntegerField(default=0)
    games_finished = models.IntegerField(default=0)
    innings_pitched = models.DecimalField(default=0, decimal_places=1, max_digits=5) # todo: check
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    total_batters_faced = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    bases_on_balls = models.IntegerField(default=0)
    strikeouts = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['year', 'player', 'team'], name="unique_pitching_stat")
        ]
