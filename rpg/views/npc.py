from rest_framework.viewsets import ModelViewSet
from ..models.npc import NPC
from ..serializers.npc import NPCSerializer
from rest_framework.permissions import IsAuthenticated

class NPCViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer