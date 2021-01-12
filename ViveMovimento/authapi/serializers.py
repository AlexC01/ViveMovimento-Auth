from rest_framework import serializers
from django.contrib.auth.models import User
from .models import food_journal

class Food_JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_journal
        fields = ['food_name', 'food_portion_quantity', 'food_macro', 'food_serving_quantity', 'macro_total']

