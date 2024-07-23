from datetime import date
from ninja import ModelSchema
from .models import Player

class FootballPlayer(ModelSchema):
  class Meta:
    model = Player
    fields = "__all__"

