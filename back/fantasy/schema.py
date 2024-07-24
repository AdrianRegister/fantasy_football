from ninja import ModelSchema, Schema
from .models import Player

class FootballPlayer(ModelSchema):
  class Meta:
    model = Player
    fields = "__all__"

class GoalscorersOut(Schema):
  name: str
  photo: str
  teamlogo: str
  goals: int

class AssistsOut(Schema):
  name: str
  photo: str
  teamlogo: str
  assists: int  

class GoalkeeperSavesOut(Schema):
  name: str
  photo: str
  teamlogo: str
  savesmade: int

class TacklesOut(Schema):
  name: str
  photo: str
  teamlogo: str
  tackles: int

class BestPerformerOut(Schema):
  name: str
  photo: str
  teamlogo: str
  g_position: str
  g_rating: str
  goals: int
  assists: int
  dribblessuccess: int
  passeskey: int
  duelswon: int
  tackles: int
  blocks: int
  interceptions: int