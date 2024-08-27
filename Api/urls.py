from django.urls import path
from .views import * 


urlpatterns = [
    path('API/', peopleAPIView.as_view()),
    path('API/<int:pk>/', peopleAPIView.as_view()),
]