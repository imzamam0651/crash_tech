from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentAPIView(APIView):
    serializer_class = StudentSerializer

    # GET method to retrieve all students
    def get(self, request):
        all_students = Student.objects.all().values()
        return Response({"Message": "List of all Students", "Student List": all_students})

    # POST method to add a new student
    def post(self, request):
        print('Request data is:', request.data)
        serializer_obj = StudentSerializer(data=request.data)
        
        # Check if the request data is valid
        if serializer_obj.is_valid():
            # Save the new student record
            student = serializer_obj.save()
            
            # Fetch the newly added student details
            student_data = Student.objects.filter(id=student.id).values()
            
            return Response({"Message": "New Student Record Added!", "Student": student_data}, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors if the request data is not valid
            return Response({"Errors": serializer_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
