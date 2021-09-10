from rest_framework import serializers
from . import models

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ('school_name', 'school_address')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('subject_name', 'subject_code', 'school')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Professor
        fields = ('name', 'school', 'subject', 'rating')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ('detail', 'professor_rate', 'professor', 'subject')