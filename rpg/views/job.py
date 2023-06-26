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
        title = self.request.query_params.get('title')
        filtersEquals = self.request.query_params.get('filtersEquals')

        queryset= queryset.filter(races__id=5)
        # Apply filters to queryset based on query parameters
        if title:
            queryset = queryset.filter(title=title)
        if filtersEquals:
            print('EQUALS =>', filtersEquals)

        return queryset