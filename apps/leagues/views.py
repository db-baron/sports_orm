from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
    context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
        # "leagues": League.objects.filter(teams__curr_players__first_name__icontains='Sophia'),
		# "players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams'),
        # "teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
        # "players": Player.objects.filter(first_name__icontains='Alexander')|Player.objects.filter(first_name__icontains='Wyatt'),
        # "players": Player.objects.filter(last_name__icontains='Cooper'),
        # 'teams': Team.objects.filter(team_name__startswith="T"),
        # 'teams': Team.objects.filter(location__icontains="Atlantic"),
        # 'teams': Team.objects.order_by('location'), # Alphabetical order
        'teams': Team.objects.order_by('-location'), # Reverse Alphabetical order
        "leagues": League.objects.exclude(sport__icontains='hockey'),
        "players": Player.objects.filter(last_name__icontains='Cooper').exclude(first_name__icontains='Joshua')

        # ORM II
        "teams": Player.objects.filter(curr_team=Team.objects.filter(team_name='Penguins')),
    }

    return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
