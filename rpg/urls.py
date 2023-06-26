from django.urls import path, include
from rest_framework import routers

from .views.character import CharacterViewSet
from .views.race import RaceViewSet
from .views.skill import SkillViewSet
from .views.npc import NPCViewSet
from .views.job import JobViewSet
from .views.user import UserViewSet
from .views.test import TestView


router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'races', RaceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'npcs', NPCViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test', TestView.as_view(), name='test'),
]
