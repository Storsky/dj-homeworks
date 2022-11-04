from django.urls import path
from . import views


urlpatterns = [
    path('sensors/<int:pk>/', views.SensorRetrieveUpdateAPIView.as_view()),
    path('sensors/', views.SensorListCreateAPIView.as_view()),
    path('measurements/', views.MeasurementsListCreateAPIView.as_view()),
    ]
