from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.
class BaseModelViewSet(ModelViewSet):
    # Override the list method to add extra functionality
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # Retrieve fields query parameter if exist, send fields dinamically to the serializer
        fields = self.request.query_params.get('fields')
        if fields:
            fields = tuple(fields.split(','))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True, fields=fields)
        return Response(serializer.data)