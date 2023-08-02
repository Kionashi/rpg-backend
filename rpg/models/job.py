from django.db import models
from .base import BaseModel

class Job(BaseModel):
    
    title = models.CharField(max_length=100)
    races = models.ManyToManyField('Race', through='JobRace')
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return f"{self.title}"