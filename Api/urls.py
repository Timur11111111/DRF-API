from django.urls import path
from .views import * 


urlpatterns = [
    path('API', peopleAPIView.as_view()),
]