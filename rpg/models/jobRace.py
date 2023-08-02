from django.db import models

from rpg.models.job import Job
from rpg.models.race import Race
from .base import BaseModel

class JobRace(BaseModel):
    job = models.ForeignKey(Job, related_name='job_race', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, related_name='job_race', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='jobs/')

    def __str__(self):
        return f"{self.job.title} - {self.race.name}"