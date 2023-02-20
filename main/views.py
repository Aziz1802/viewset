from django.shortcuts import render
from .models import * 
from rest_framework import viewsets
from rest_framework import response
from .serializer import StudentSerializer
# from django.shortcuts import get_object_or_404

class StudentView(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    # seril = StudentSerializer
    serializer_class = StudentSerializer


    # def list(self,request):
    #     queryset= Student.objects.all()
    #     serializer = StudentSerializer(queryset,many=True)
    #     return response.Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentSerializer(user)
    #     return response.Response(serializer.data)
