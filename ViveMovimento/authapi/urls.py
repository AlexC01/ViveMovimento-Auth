from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('api-food/', apiOverview, name = 'api-food'),
    path('api-food/food-journal/', foodList, name = 'food-journal'),
    path('api-food/food-journal-detail/<str:uuid>', foodjournalDetail, name = 'food-journal-detail'),
    path('api-food/food-create/', foodCreate, name = 'food-create'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]