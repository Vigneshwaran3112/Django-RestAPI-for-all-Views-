from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from .models import Employee

class employeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

class employeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

















# Alternative code using mixins:

# class employeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




# Alternative code for customization using generic:,

# class employeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         queryset = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(queryset)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         queryset = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(queryset, data=request.data)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         queryset = Employee.objects.get(pk=pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

