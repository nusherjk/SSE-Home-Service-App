import datetime
from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

from .permissions import UserIsCompletedMixin

# Create your views here.
PENDING ='Pending'
ACCEPTED = 'Accepted'
COMPLETED = 'Completed'
CANCELLED = 'Cancelled'

class IndexView(TemplateView):
    # template_name = 'landing.html'
    template_name = 'mainbody.html'


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
class ServiceDetailView(LoginRequiredMixin, TemplateView):
    service_model = Service
    provider_model = ProviderProfile
    template_name = 'services/service_detail.html'
    # context_object_name = 'service'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = self.service_model.objects.get(id=self.kwargs['service_id'])
        context['providers'] = self.provider_model.objects.filter(services=context['service']).exclude(user=self.request.user)
        return context

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
class BookingCreateView(UserIsCompletedMixin, LoginRequiredMixin, TemplateView):
    model = Booking
    service_model = Service
    provider_model = ProviderProfile
    # form_class = BookingForm
    template_name = 'booking/booking_form.html'
    # success_url = reverse_lazy('booking-list')


    def get_context_data(self, **kwargs):
        print("HAHA")
        context = super().get_context_data(**kwargs)
        context['service'] = self.service_model.objects.get(id=self.kwargs['service_id'])
        context['provider'] = self.provider_model.objects.get(id=self.kwargs['provider_id'])
        context['total'] =  context['service'].price + (Decimal(context['provider'].hourly_rate) * Decimal(context['service'].duration.total_seconds()) / Decimal(3600) )
        context['GST'] =  context['total']/10 # 10%
        return context



    def post(self, *args, **kwargs):
        # print(self.request.POST)

        duration = self.service_model.objects.get(id=self.kwargs['service_id']).duration
        startTimeDate = datetime.datetime.combine(date=datetime.datetime.strptime(self.request.POST['ddate'], '%Y-%m-%d').date(),
                                                  time=datetime.datetime.strptime(self.request.POST['dtime'], '%H:%M').time())
        endTimeDate = startTimeDate+ duration
        booking = Booking.objects.create(
            customer=self.request.user,
            service=self.service_model.objects.get(id=self.kwargs['service_id']),
            provider=self.provider_model.objects.get(id=self.kwargs['provider_id']),
            address=self.request.POST['daddress'],
            date=self.request.POST['ddate'],
            time=self.request.POST['dtime'],
            end_date= endTimeDate.date(),
            end_time=endTimeDate.time()
                                         )
        booking.save()

        return redirect('services')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)




# List all bookings for the logged-in customer
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

# Detail view for a specific booking
# TODO:
class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking'


class ServiceCompleteView(LoginRequiredMixin):
    # TODO:
    pass


# Update a booking (e.g., reschedule)
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

# Cancel a booking (sets status to 'Cancelled')
class BookingCancelView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('booking-requests')  # Replace 'history-page' with your target URL name
    def get(self, *args, **kwargs):

        # Call a function to update the history (implement your history update logic here)
        booking = Booking.objects.get(id= kwargs['id'])
        booking.status = CANCELLED
        booking.save()

        # Continue with the redirection
        return super().get(self.request, *args, **kwargs)

class BookingCancelbyInitiatorView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('bookings')  # Replace 'history-page' with your target URL name
    def get(self, *args, **kwargs):

        # Call a function to update the history (implement your history update logic here)
        booking = Booking.objects.get(id= kwargs['id'])
        if booking.status != ACCEPTED:
            booking.status = CANCELLED
            booking.save()



        # Continue with the redirection
        return super().get(self.request, *args, **kwargs)

class BookingAcceptView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('booking-requests')  # Replace 'history-page' with your target URL name

    def get(self, *args, **kwargs):
        # Call a function to update the history (implement your history update logic here)
        booking = Booking.objects.get(id=kwargs['id'])
        booking.status = ACCEPTED
        booking.save()

        # Continue with the redirection
        return super().get(self.request, *args, **kwargs)



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


class ProviderBooks(LoginRequiredMixin, TemplateView):
    template_name = 'providers/Booking_requests.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.filter(provider__user=self.request.user, status='PENDING')
        return context



class ProviderBookings(LoginRequiredMixin, TemplateView):
    template_name = 'providers/Booking_history.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.filter(provider__user=self.request.user)
        return context

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
