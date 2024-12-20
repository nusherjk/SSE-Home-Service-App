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
from django.contrib.auth import views as auth_views
# from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView
# from .views import RegisterViewSet
# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )
from django.conf import settings
from django.conf.urls.static import static
from .views import NewLoginView, RegisterView, ProfileView, UpdateProfileView

# , send_otp, verify_otp)
# from .views import UserViewSet
urlpatterns = [
    path('login/', NewLoginView.as_view(), name="login"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('profile', ProfileView.as_view(), name="profile"),
    path('profileupdate', UpdateProfileView.as_view(), name="profile-update"),

]
