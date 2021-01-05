from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class employeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        emp = request.POST
        serializers = EmployeeSerializer(Employee.objects.create(first_name=emp['first_name'], last_name=emp['last_name'], emp_no=emp['emp_no']))
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        emp = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Employee.objects.all()
        emp = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Employee.objects.all()
        emp = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Employee.objects.all()
        emp = get_object_or_404(queryset, pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
