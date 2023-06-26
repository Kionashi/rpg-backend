from django.db import models
from .entity import BaseEntity
class NPC(BaseEntity):
    class Factions(models.IntegerChoices):
       ALLY = 1,
       ENEMY = 2,
       NEUTRAL = 3,
    
    faction = models.IntegerField(choices=Factions.choices, default=Factions.NEUTRAL)

    def __str__(self):
        return f"Name: {self.name} - Level: {self.level} - Faction: {self.get_faction_display()}"