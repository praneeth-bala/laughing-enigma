from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import XML
from .serializers import XMLSerializer

from .utils import is_malicious

class XMLApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'xml': request.data.get('xml')
        }
        serializer = XMLSerializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            return Response({"is_malicious": is_malicious(data['xml'])}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)