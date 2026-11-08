from django.shortcuts import render
from .models import Person1
from .serializers import Person1Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

class PersonListView(APIView):
    def get(self,request):
        persons=Person1.objects.all()
        serializier=Person1Serializer(persons,many=True)
        return Response(serializier.data)
        
    def post(self,request):
        serializer=Person1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors)
    

class PersonUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person1.objects.all()
    serializer_class=Person1Serializer