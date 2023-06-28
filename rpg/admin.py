from django.contrib import admin
from .models.character import Character
from .models.npc import NPC
from .models.race import Race
from .models.job import Job
from .models.jobRace import JobRace
from .models.skill import Skill

# Register your models here.
admin.site.register(Character)
admin.site.register(NPC)
admin.site.register(Race)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(JobRace)

