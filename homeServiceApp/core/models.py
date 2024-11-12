import datetime
from datetime import timedelta
from decimal import Decimal

from django.db import models


# Service Category (e.g., Plumbing, Cleaning, Electrical)
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Service offered by providers
class Service(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(default=timedelta(hours=2))

    def __str__(self):
        return f"{self.name} - {self.category.name}"


# Profile for service providers
class ProviderProfile(models.Model):
    user = models.OneToOneField("accounts.Customer", on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    years_of_experience = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    bio = models.TextField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


# Service bookings made by customers
class Booking(models.Model):
    customer = models.ForeignKey("accounts.Customer", related_name='bookings', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    address = models.ForeignKey('accounts.Address', related_name='booking_address', on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Expired', 'Expired'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def calculate_total_price(self):
        # Service charge (already stored in the 'price' field)
        service_charge = self.service.price

        # Provider's hourly rate (assumed to be from the ProviderProfile model)
        hourly_rate = Decimal(self.provider.hourly_rate)

        # Convert duration (timedelta) to hours
        job_duration_in_hours = Decimal(self.service.duration.total_seconds() / 3600)  # Convert seconds to hours

        # Calculate the total price
        total_price = service_charge + (hourly_rate * job_duration_in_hours)

        return total_price

    def check_and_update_date(self):
        """
        Checks if `self.date` is greater than `comparison_date` and updates it if necessary.
        """
        if self.date < datetime.datetime.now().date():
            # Update the field or any logic you need to apply
            if self.status == 'Accepted':
                self.status = 'Expired'  # Example of updating it to the current date
                self.save()  # Save the changes to the database

    def __str__(self):
        return f"Booking by {self.customer.username} for {self.service.name}"


# Review model for customers to rate service providers
class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f"Review by {self.customer.username} for {self.provider.user.username}"


# Payment details for services
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method_choices = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Cash', 'Cash'),
    ]
    payment_method = models.CharField(max_length=20, choices=payment_method_choices)

    def __str__(self):
        return f"Payment for {self.booking.service.name} by {self.booking.customer.username}"
