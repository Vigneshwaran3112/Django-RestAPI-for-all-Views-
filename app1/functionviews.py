from django.http import Http404, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee
from django.core import serializers as jsontoxml

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def employeeList(request, pk=None, format=None):

    if request.method == 'GET':
        print(format)
        if pk:
            emp = Employee.objects.get(pk=pk)
            serializers = EmployeeSerializer(emp)
            return Response(serializers.data, content_type='application/xml')
        else:
            emp = Employee.objects.all()
            serializers = EmployeeSerializer(emp, many=True)
            return Response(serializers.data)

    if request.method == 'POST':
        
        emp = request.POST
        serializers = EmployeeSerializer(Employee.objects.create(first_name=emp['first_name'], last_name=emp['last_name'], emp_no=emp['emp_no']))
        return Response(serializers.data)

    if request.method == 'PUT':
        serializers = EmployeeSerializer(Employee.objects.get(pk=pk), data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    if request.method == 'PATCH':
        serializers = EmployeeSerializer(Employee.objects.get(pk=pk), data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    if request.method == 'DELETE':
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def xmlview(request):

    emp = Employee.objects.all()
    data = jsontoxml.serialize("xml", emp)
    return HttpResponse(data, content_type='text/xml')

