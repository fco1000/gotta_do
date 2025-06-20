# from django.shortcuts import render
from rest_framework import generics
from journal.serializers import JournalSerializer
from journal.models import Journal

# Create your views here.
class JournalCreate(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    lookupfield = "pk"