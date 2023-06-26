from rest_framework import viewsets
from ..serializers.user import UserSerializer
from django.contrib.auth.models import User
from ..services.authentication import AuthenticationService
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    auth_service = AuthenticationService()

   
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = self.auth_service.generate_token(user)
        response_data = {
            'user': serializer.data,
            'token': token,
        }
        serializer.data['token'] = token 
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)