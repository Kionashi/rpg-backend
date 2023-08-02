from rest_framework import serializers
from ..models.jobRace import JobRace

class JobRaceSerializer(serializers.ModelSerializer):
    race_name = serializers.SerializerMethodField()
    job_name = serializers.SerializerMethodField()
    class Meta:
        model = JobRace
        fields = ['id', 'race', 'job', 'race_name', 'job_name', 'image']

    def get_race_name(self, obj):
        return obj.race.name

    def get_job_name(self, obj):
        return obj.job.title
    