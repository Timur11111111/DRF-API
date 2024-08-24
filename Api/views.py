from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import peopleSerializer
from .models import people
from rest_framework.permissions import AllowAny

class peopleAPIView(APIView):
    queryset = people.objects.all()
    serializer_class = peopleSerializer
    permission_classes = [AllowAny]
    def get(self, request):
        events = people.objects.all()
        serializer = peopleSerializer(events, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = peopleSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        event = request.data.get()
        if not event:
            return Response({"error": "No IDs provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        people.objects.filter(id__in=event).delete

        return Response({"message": "People deleted successfully."}, status=status.HTTP_204_NO_CONTENT)