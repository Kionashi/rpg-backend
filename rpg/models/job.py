from django.db import models
from .base import BaseModel

class Job(BaseModel):
    
    title = models.CharField(max_length=100)
    races = models.ManyToManyField('Race')
    skills = models.ManyToManyField('Skill')
    image = models.ImageField(null=True, blank=True, upload_to='jobs/')

    def __str__(self):
        return f"{self.title}"