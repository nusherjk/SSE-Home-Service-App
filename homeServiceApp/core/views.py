from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'landing.html'


class DashboardView(TemplateView, LoginRequiredMixin):
    template_name = 'Dashboard.html'



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import get_object_or_404, redirect
from .models import Service, ProviderProfile, Booking, Review, Payment
from .forms import BookingForm, ReviewForm

# List all available services
class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    paginate_by = 10  # Add pagination if you have many services

# Detail view for a specific service
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

# List service providers
class ProviderListView(ListView):
    model = ProviderProfile
    template_name = 'providers/provider_list.html'
    context_object_name = 'providers'
    paginate_by = 10

# Detail view for a service provider
class ProviderDetailView(DetailView):
    model = ProviderProfile
    template_name = 'providers/provider_detail.html'
    context_object_name = 'provider'

# Create a booking (only available for logged-in customers)
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

# List all bookings for the logged-in customer
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

# Detail view for a specific booking
class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'

# Update a booking (e.g., reschedule)
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

# Cancel a booking (sets status to 'Cancelled')
class BookingCancelView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['status']
    template_name = 'bookings/booking_cancel.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.status = 'Cancelled'
        return super().form_valid(form)

# Create a review for a completed booking
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.booking = get_object_or_404(Booking, id=self.kwargs['booking_id'])
        form.instance.provider = form.instance.booking.provider
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking-detail', kwargs={'pk': self.kwargs['booking_id']})

# List all reviews for a specific provider
class ProviderReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        provider = get_object_or_404(ProviderProfile, pk=self.kwargs['provider_id'])
        return Review.objects.filter(provider=provider)

# Process payment for a booking
class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    fields = ['amount', 'payment_method']
    template_name = 'payments/payment_form.html'

    def form_valid(self, form):
        booking = get_object_or_404(Booking, pk=self.kwargs['booking_id'])
        form.instance.booking = booking
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking-detail', kwargs={'pk': self.kwargs['booking_id']})
