from django.urls import path

from .views import StudentAPIView

urlpatterns = [
   path("api/student", StudentAPIView.as_view()),
]