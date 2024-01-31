from rest_framework import serializers
from .models import ProblemsModel

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsModel
        fields = ['title','description','difficulty','test_cases']