from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse

import time
from asgiref.sync import sync_to_async
import asyncio

from .models import Team, Player, BattingStatistics, PitchingStatistics

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'players/index.html'
    context_object_name = 'team_list'
    # todo: show players not on teams

    def get_queryset(self):
        return Team.objects.order_by('org_abbreviation')

class PlayerView(generic.DetailView):
    model = Player
    template_name = 'players/player.html'

class TeamView(generic.DetailView):
    model = Team
    template_name = 'players/team.html'
    # context_object_name = 'player_list'

    # def get_queryset(self):
    #     print(self)
    #     return Player.objects.filter(team=self.id).order_by('name_last', 'name_use')
    
# def get_team_players(request, team_id):
#     team = get_object_or_404(Team, pk=team_id)
#     return Player.objects.filter(team=team).order_by('name_last', 'name_use')

# async def player_view(request, pk):
#     # player = get_object_or_404(Player, pk=pk)
#     # return render(request, 'players/player.html', {'player': player})
#     # view = PlayerView.as_view()
#     # response = view(request, pk=pk)
#     response = await async_view(request)
#     # rendered = render(response, 'players/player.html')
#     # rendered = render(response, 'players/stats.html')
#     # rendered = async_view(request)
#     print('-----------response----------')
#     print(response)
#     test = await Player.get_batting_statistics(player_id=pk)
#     print('--------test-----')
#     print(test)
#     context = {
#         'message': 'from player_view',
#         # 'other_view': response.content.decode('utf-8'),
#         # 'other_view': response,
#         # 'other_view': rendered
#         'test': test,
#     }
#     return render(request, 'players/player2.html', context)


# class TeamListView(generic.ListView):
#     model = Team
#     template_name = 'team_list.html'

# @sync_to_async
# def get_batting_stats_async():
#     print('getting batting stats...')
#     time.sleep(2)
#     qs = Player.objects.all() # todo change
#     print(qs)
#     print('all players fetched')

# @sync_to_async
# def get_pitching_stats_async():
#     print('getting pitching stats...')
#     time.sleep(5)
#     qs = Team.objects.all() # todo: change
#     print(qs)
#     print('all teams fetched')

# async def async_view(request):
#     start_time = time.time()
#     stats = await asyncio.gather(get_batting_stats_async(), get_pitching_stats_async())
#     print('------stats-------')
#     print(stats)
#     total = time.time() - start_time
#     # return HttpResponse(f"time taken async {total}")
#     return render(request, 'players/stats.html', {})
