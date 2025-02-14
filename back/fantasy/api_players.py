from ninja import NinjaAPI
import json
from .models import Player
from .schema import GoalscorersOut, AssistsOut, GoalkeeperSavesOut, TacklesOut, BestPerformerOut
from typing import List

players_api = NinjaAPI()

@players_api.get("best-performers", response=List[BestPerformerOut])
def get_best_performers(request, position):
  position = position.capitalize()
  return Player.objects.filter(g_rating__gt=7, g_position=position).order_by('-g_rating')[:10]

@players_api.get("tackles", response=List[TacklesOut])
def get_tackles(request):
  return Player.objects.filter(tackles__gt=0).order_by('-tackles')[:10]

@players_api.get("saves", response=List[GoalkeeperSavesOut])
def get_saves(request):
  return Player.objects.filter(savesmade__gt=0).order_by('-savesmade')[:10]

@players_api.get("assists", response=List[AssistsOut])
def get_assists(request):
  return Player.objects.filter(assists__gt=0).order_by('-assists')[:10]

@players_api.get("goalscorers", response=List[GoalscorersOut])
def get_goals(request):
  return Player.objects.filter(goals__gt=0).order_by('-goals')[:10]

@players_api.patch("update-players")
def store_data(request):
  page = 1
  while page <= 51:
    with open(f"./player-data/page{page}.json", "r") as file:
      data = json.load(file)
      players = data["response"]

    for player in players: 
      player_info = player["player"]
      stats = player["statistics"][0]

      Player.objects.create(
        playerid=player_info["id"],
        name=player_info["name"],
        firstname=player_info["firstname"],
        lastname=player_info["lastname"],
        age=player_info["age"],
        birthdate=player_info["birth"]["date"],
        nationality=player_info["nationality"],
        height=player_info["height"],
        weight=player_info["weight"],
        injured=player_info["injured"],
        photo=player_info["photo"],
        teamid=stats["team"]["id"],
        teamname=stats["team"]["name"],
        teamlogo=stats["team"]["logo"],
        leagueseason=stats["league"]["season"],
        g_apps=stats["games"]["appearences"],
        g_starts=stats["games"]["lineups"],
        g_minutes=stats["games"]["minutes"],
        g_position=stats["games"]["position"],
        g_rating=stats["games"]["rating"],
        shotstotal=stats["shots"]["total"],
        shotsontarget=stats["shots"]["on"],
        goals=stats["goals"]["total"],
        goalsconceded=stats["goals"]["conceded"],
        savesmade=stats["goals"]["saves"],
        assists=stats["goals"]["assists"],
        passestotal=stats["passes"]["total"],
        passeskey=stats["passes"]["key"],
        tackles=stats["tackles"]["total"],
        blocks=stats["tackles"]["blocks"],
        interceptions=stats["tackles"]["interceptions"],
        duelstotal=stats["duels"]["total"],
        duelswon=stats["duels"]["won"],
        dribblesattempted=stats["dribbles"]["attempts"],
        dribblessuccess=stats["dribbles"]["success"],
        foulsagainst=stats["fouls"]["drawn"],
        foulscommitted=stats["fouls"]["committed"],
        cardsyellow=stats["cards"]["yellow"],
        cardsred=stats["cards"]["red"],
        cardsyellowred=stats["cards"]["yellowred"],
        penaltieswon=stats["penalty"]["won"],
        penaltiesconceded=stats["penalty"]["commited"],
        penaltiesscored=stats["penalty"]["scored"],
        penaltiesmissed=stats["penalty"]["missed"],
        penaltiessaved=stats["penalty"]["saved"],
      )

    page += 1    

  return {"success": True}