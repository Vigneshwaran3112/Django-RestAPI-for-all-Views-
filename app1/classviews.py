from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee

# Create your views here.
class employeeList(APIView):
    
    def get(self, request, pk=None):
        if pk:
            serializer = EmployeeSerializer(Employee.objects.get(pk=pk))
        else:
            serializer = EmployeeSerializer(Employee.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        e = request.data
        d = Employee.objects.create(first_name=e['first_name'], last_name=e['last_name'], emp_no=e['emp_no'])
        d.save()
        serializer = EmployeeSerializer(d)
        return Response(serializer.data)

    def put(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class employeeDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         emp = self.get_object(pk)
#         serializer = EmployeeSerializer(emp)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         emp = self.get_object(pk)
#         serializer = EmployeeSerializer(emp, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         emp = self.get_object(pk)
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


