# from django.shortcuts import render
from rest_framework import generics
from tasks.models import Task
from tasks.serializer import TaskSerializer

class TaskCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookupfield = "pk"