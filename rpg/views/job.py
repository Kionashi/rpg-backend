from ..models.job import Job
from ..serializers.job import JobSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class JobViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Retrieve query parameters from request
        race = self.request.query_params.get('race')
        # Apply filters to queryset based on query parameters
        if race:
           queryset = queryset.filter(jobrace__race_id=5).prefetch_related('jobrace_set').values('id', 'created_at', 'updated_at', 'title', 'jobrace')

        return queryset