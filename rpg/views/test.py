from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.race import Race
from ..serializers.race import RaceSerializer

class TestView(APIView):
    def get(self, request):
        races = Race.objects.all()
        serializer = RaceSerializer(races, many=True)
        # Your logic for handling GET requests
        return Response(serializer.data)

    def post(self, request):
        # Your logic for handling POST requests
        return Response("POST response")
