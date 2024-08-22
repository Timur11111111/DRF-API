from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import peopleSerializer
from .models import people

class peopleAPIView(APIView):
    serializer_class = peopleSerializer
    def get(self, request):
        events = people.objects.all()
        serializer = peopleSerializer(events, many=True, context={'request': request} )
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.
