from .models import Person1
from rest_framework import serializers

class Person1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Person1
        fields = ['id','first_name','last_name','email','age']