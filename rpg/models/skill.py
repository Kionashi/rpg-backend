from django.db import models
from .base import BaseModel
class Skill(BaseModel):
    class Attributes(models.TextChoices):
        STR = 'str'
        DEX = 'dex'
        INT = 'int'
    
    class SkillTypes(models.TextChoices):
        DAMAGE = 'damage'
        HEAL = 'heal'
        BUFF = 'buff'
        DEBUFF = 'debuff'
    
    name = models.CharField(max_length=100)
    side_effect_skill = models.ForeignKey("Skill", on_delete=models.SET_NULL, blank=True, null=True)
    level_required = models.PositiveSmallIntegerField(default=1)
    damage = models.IntegerField(default=1)
    cost = models.IntegerField(default=1)
    modifier = BaseModel.PositiveDecimalField(max_digits=7, decimal_places=2)
    type = models.CharField(max_length=6, choices=SkillTypes.choices, default=SkillTypes.DAMAGE)
    duration = models.PositiveSmallIntegerField(default=1)
    attribute = models.CharField(max_length=3, choices=Attributes.choices, default=Attributes.STR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"