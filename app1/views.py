from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer

#class based

class EmployeeView(APIView):
    def get(self, request):
        employeeobj = Employee.objects.all()
        serializer = EmployeeSerializer(employeeobj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


