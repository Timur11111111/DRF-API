from rest_framework import serializers
from .models import people

class peopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = people
        fields = ['id', 'firstname', 'lastname', 'age']