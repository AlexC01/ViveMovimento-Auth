from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from .serializers import Food_JournalSerializer
from .models import food_journal

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/food-journal/',
        'Detail Food': '/food-journal-detail/<str:uuid>/',
        'Create': '/food-create/',
    }
    return Response(api_urls)

@api_view(['GET'])
def foodList(request):
    foods = food_journal.objects.all()
    serializer = Food_JournalSerializer(foods, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def foodjournalDetail(request, uuid):
    foods = food_journal.objects.filter(uuid = uuid)
    serializer = Food_JournalSerializer(foods, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def foodCreate(request):
    serializer = Food_JournalSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
