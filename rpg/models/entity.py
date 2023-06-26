from django.db import models
from .base import BaseModel

class BaseEntity(BaseModel):
    class Status(models.IntegerChoices):
        NEUTRAL     = 1
        DEAD        = 2
        UNDEAD      = 3
        POISONED    = 4
        FROZEN      = 5
        SHOKED      = 6
        CASTING     = 7
        RESTING     = 8
        ENRAGED     = 9
        STUNNED     = 10
        REGENERATING= 11

    name = models.CharField(max_length=100)
    race = models.ForeignKey("Race", on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=1)
    mp = models.IntegerField(default=1)
    str = models.IntegerField(default=1)
    dex = models.IntegerField(default=1)
    int = models.IntegerField(default=1)
    status = models.IntegerField(choices=Status.choices, default=Status.NEUTRAL)
    image = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
