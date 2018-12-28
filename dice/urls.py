"""robot URL Configuration
"""
from django.conf.urls import url

from django.urls import path
from dice.views import home, ajax_bet, ajax_my_games, ajax_games_history
from dice.views import get_clock, get_game_abi, get_game_contract
from dice.views import temp_devel_shit_deleteme

urlpatterns = [
    # common views
    url(r'^$', home, name='home'),
    # ajax
    url(r'^ajax/bet$', ajax_bet, name='ajax_bet'),
    url(r'^ajax/tabulky/games/all$', ajax_games_history, name='ajax_games_history'),
    url(r'^ajax/tabulky/games/mine$', ajax_my_games, name='ajax_my_games'),
    # bytecode, abi, clock
    url(r'^abi$', get_game_abi, name='get_game_abi'),
    url(r'^contract$', get_game_contract, name='get_game_contract'),
    url(r'^clock$', get_clock, name='get_clock'),
    # temp stuff
    url(r'^devel', temp_devel_shit_deleteme, name='temp_devel_shit_deleteme'),
]
