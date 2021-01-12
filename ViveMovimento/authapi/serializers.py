from rest_framework import serializers
from django.contrib.auth.models import User
from .models import food_journal

class Food_JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_journal
        fields = '__all__'

