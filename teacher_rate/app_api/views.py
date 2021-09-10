from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class SchoolView(viewsets.ModelViewSet):
    serializer_class = serializers.SchoolSerializer
    queryset = models.School.objects.all()

class ProfessorView(viewsets.ModelViewSet):
    serializer_class = serializers.ProfessorSerializer
    queryset = models.Professor.objects.all()

class SubjectView(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer
    queryset = models.Subject.objects.all()

class ReviewView(viewsets.ModelViewSet):
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()