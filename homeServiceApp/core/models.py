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
        return self.user.username


# Service bookings made by customers
class Booking(models.Model):
    customer = models.ForeignKey("accounts.Customer", related_name='bookings', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    address = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')

    def __str__(self):
        return f"Booking by {self.customer.username} for {self.service.name}"


# Review model for customers to rate service providers
class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()

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