from django.http import HttpResponseForbidden

from .models import Booking


class UserIsCompletedMixin:
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is authenticated and has `is_completed` set to True
        if not request.user.is_authenticated or not request.user.is_completed:
            return HttpResponseForbidden("You do not have permission to access this view.")
        return super().dispatch(request, *args, **kwargs)


class OwnerofBookingMixin:
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is authenticated and has `is_completed` set to True
        booking = Booking.objects.get(id=kwargs['id'])
        if not request.user.is_authenticated or request.user != booking.customer:
            return HttpResponseForbidden("You do not have permission to access this view.")

        return super().dispatch(request, *args, **kwargs)


class BookingAllreadyDoneMixin:
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is authenticated and has `is_completed` set to True
        booking = Booking.objects.get(id=kwargs['id'])
        if not request.user.is_authenticated or( request.user != booking.provider or  booking.status != 'PENDING'):
            return HttpResponseForbidden("You cannot accept an already accepted booking.")

        return super().dispatch(request, *args, **kwargs)