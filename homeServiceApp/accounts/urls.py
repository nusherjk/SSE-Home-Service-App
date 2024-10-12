"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import  views as auth_views
# from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView
# from .views import RegisterViewSet
# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )
from django.conf import settings
from django.conf.urls.static import static
from .views import NewLoginView, RegisterView
# , send_otp, verify_otp)
# from .views import UserViewSet
urlpatterns = [
    path('login', NewLoginView.as_view(), name="login"),
    # path('oauth/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('register', RegisterView.as_view(), name="register"),
    # path('oauth/google/login/', google_login, name='google-direct-login'),
    # path('getEmpInfo/<emp_id>', getEmpInfo, name="getEmpInfo"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),

    # path('send-otp/', send_otp, name='send_otp'),
    # path('verify-otp/', verify_otp, name='verify_otp'),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('profile', UserViewSet.as_view(), name='profile'),


    # path('api-auth/', include('rest_framework.urls')),

]
