from django.urls import path, include
from . import views
from .views import FacebookLogin

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
]