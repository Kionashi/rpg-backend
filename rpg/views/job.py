from ..models.job import Job
from ..serializers.job import JobSerializer
from rest_framework.viewsets import ModelViewSet
from .base import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models.jobRace import JobRace
from django.db import models
from rest_framework.response import Response
# Create your views here.
class JobViewSet(BaseModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Retrieve query parameters from request
        race = self.request.query_params.get('race')
        # Apply filters to queryset based on query parameters
        if race:
           queryset = queryset.filter(job_race__race_id=race).prefetch_related(
                models.Prefetch('job_race', queryset=JobRace.objects.filter(race_id=race))
            )
        return queryset
    
    