from django.db import models
from .entity import BaseEntity
class Character(BaseEntity):
    exp = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
    