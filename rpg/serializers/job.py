from rest_framework import serializers
from ..models.job import Job
from .skill import SkillSerializer
from .jobRace import JobRaceSerializer
from .base import DynamicFieldsModelSerializer

class JobSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Job
        fields =  ['id', 'title','races','skills', 'job_race']
        # fields = '__all__'
        depth = 1
