from rest_framework import serializers
from .models import XML
class XMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = XML
        fields = ["xml"]