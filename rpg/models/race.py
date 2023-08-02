from django.db import models
from .base import BaseModel

class Race(BaseModel):
    name = models.CharField(max_length=100)
    hp_growth = BaseModel.PositiveDecimalField(max_digits=7, decimal_places=2)
    mp_growth = BaseModel.PositiveDecimalField(max_digits=7, decimal_places=2)
    str_growth = BaseModel.PositiveDecimalField(max_digits=7, decimal_places=2)
    int_growth = BaseModel.PositiveDecimalField(max_digits=7, decimal_places=2)
    dex_growth = BaseModel.PositiveDecimalField(max_digits=7, decimal_places=2)
    base_hp = models.PositiveSmallIntegerField(default=1)
    base_mp = models.PositiveSmallIntegerField(default=1)
    base_str = models.PositiveSmallIntegerField(default=1)
    base_int = models.PositiveSmallIntegerField(default=1)
    base_dex = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(default=None)
    description= models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - HP Growth: {self.hp_growth} - MP Growth: {self.mp_growth} - STR Growth: {self.str_growth} - INT Growth: {self.int_growth} - DEX Growth: {self.dex_growth}"