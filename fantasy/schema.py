from ninja import ModelSchema, Schema
from .models import Player

class FootballPlayer(ModelSchema):
  class Meta:
    model = Player
    fields = "__all__"

class GoalscorersOut(Schema):
  name: str
  photo: str
  goals: int