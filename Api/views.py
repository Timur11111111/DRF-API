from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import peopleSerializer
from .models import people
from rest_framework.permissions import AllowAny

class peopleAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        events = people.objects.all()
        serializer = peopleSerializer(events, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = peopleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        ids = request.data.get('ids', [])  # Получаем список ID из запроса
        if not ids:
            return Response({"error": "No IDs provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Удаляем объекты с указанными ID
        deleted_count, _ = people.objects.filter(id__in=ids).delete()
        
        return Response({"message": f"{deleted_count} people deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
