from rest_framework import serializers
from .models import Employee
global obj
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # msg = serializers.SerializerMethodField()
    # msg = serializers.CharField(max_length=30)

    class Meta:
        model = Employee
        fields = ['url','first_name', 'last_name', 'emp_no']

    # def get_msg(self, obj):
    #     return 'hi'
    # def validate_msg(self, value):
    #     return value    
        
    # def to_representation(self, value):

    #     val = {
    #         'first_name': value.first_name,
    #         'last_name': value.last_name,
    #         'emp_no': value.emp_no,
    #         'msg': 'hi'
    #     
    #     return val


class UserDataCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return self.child.objects.bulk_create(books)

class UserDataSerializer(serializers.Serializer):
    class Meta:
        list_serializer_class = UserDataCreateSerializer


