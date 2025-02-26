from django.contrib import admin

from .models import Team, Player, BattingStatistics, PitchingStatistics

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(BattingStatistics)
admin.site.register(PitchingStatistics)