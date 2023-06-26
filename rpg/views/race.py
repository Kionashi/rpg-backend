from ..models.race import Race
from ..serializers.race import RaceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RaceViewSet(ModelViewSet):
    model = Race
    serializer_class = RaceSerializer
    queryset = Race.objects.all()

