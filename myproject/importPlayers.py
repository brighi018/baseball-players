# run using python3 manage.py shell and then
# with open('importPlayers.py') as f:
#     exec(f.read())

# run using
# python3 manage.py shell < importPlayers.py 

# print('test')

import json

# todo: get file to import as argument
with open('players.json', 'r') as file:
    data = json.load(file)

# print(data)

from players.models import Player, Team, PitchingStatistics, BattingStatistics

for p in data:
    # print('id: ', p['id'])

    # test = Team.objects.create(org_abbreviation=p['team'])
    team, team_created = Team.objects.get_or_create(
        org_abbreviation=p['team']
        # defaults={}
    )
    # print('team: ', team)
    # print('created: ', team_created)

    # todo: check if player id already exists
    player, player_created = Player.objects.get_or_create(
        id=p['id'],
        defaults={
            'name_first': p['name_first'],
            'name_use': p['name_use'],
            'name_last': p['name_last'],
            'team': team,
            'birth_date': p['birth_date'],
            'height_feet': p['height_feet'],
            'height_inches': p['height_inches'],
            'weight': p['weight'],
            'throws': p['throws'],
            'bats': p['bats'],
            'primary_position': p['primary_position'],
        }
    )
    # print('player: ', player)
    # print('created: ', player_created)
    if not player_created:
        # player.save()
        print('player already exists: ', player.id)
        # todo: could update existing player with info

    # for s in p['stats']['batting']:
    #     stat_team, stat_team_created = Team.objects.get_or_create(
    #         org_abbreviation=p['team']
    #         # defaults={}
    #     )
    #     stat, created = BattingStatistics.objects.get_or_create(
    #         player=player,
    #         year=s['year'],
    #         team=stat_team,
    #         defaults={
    #             **s
    #         }
    #     )

    statTypes = [
        { 'key': 'batting', 'model': BattingStatistics },
        { 'key': 'pitching', 'model': PitchingStatistics },
    ]
    for statType in statTypes:
        for s in p['stats'][statType['key']]:
            stat_team, stat_team_created = Team.objects.get_or_create(
                org_abbreviation=p['team']
                # defaults={}
            )
            stat, created = statType['model'].objects.get_or_create(
                player=player,
                year=s['year'],
                team=stat_team,
                defaults={
                    **s
                }
            )
    
