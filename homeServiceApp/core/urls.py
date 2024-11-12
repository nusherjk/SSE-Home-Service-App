"""
URL configuration for homeServiceApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('services/<service_id>/', ServiceDetailView.as_view(), name='services'),
    path('createBooking/<service_id>/<provider_id>/', BookingCreateView.as_view(), name='createBooking'),
    path('bookings', BookingListView.as_view(), name='bookings'),
    path('bookings/<id>/cancel', BookingCancelbyInitiatorView.as_view(), name='bookings-cancel-by-initiator'),
    path('bookings/<id>/complete', BookingCompletedView.as_view(), name='bookings-completed'),
    path('review/<booking_id>/', ReviewCreateView.as_view(), name='bookings-review'),
    path('providers/', ProviderListView.as_view(), name='providers'),
    path('providers/<id>/', ProviderDetailView.as_view(), name='providers'),
    path('booking-requests/', ProviderBooks.as_view(), name='booking-requests'),
    path('booking-history/', ProviderBookings.as_view(), name='booking-history'),
    path('booking-requests/<id>/cancel', BookingCancelView.as_view(), name='booking-cancel'),
    path('booking-requests/<id>/accept', BookingAcceptView.as_view(), name='booking-accept'),

    # path('login', LoginView.as_view(), name='login'),
]
