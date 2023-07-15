from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import XML
from .serializers import XMLSerializer

from .utils import empty

class XMLApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'xml': request.data.get('xml')
        }
        serializer = XMLSerializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            return Response({"array":empty()}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)