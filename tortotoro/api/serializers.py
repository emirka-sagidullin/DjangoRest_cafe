from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class StatusSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'