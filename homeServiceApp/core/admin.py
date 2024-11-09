from django.contrib import admin
from .models import  ServiceCategory, Service, ProviderProfile, Booking, Review, Payment


# Customize the admin view for ServiceCategory
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Customize the admin view for Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

# Customize the admin view for ProviderProfile
@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'years_of_experience', 'hourly_rate', 'rating')
    list_filter = ('years_of_experience',)
    search_fields = ('user__username', 'bio')
    filter_horizontal = ('services',)

# Inline configuration for showing reviews in Booking admin view
class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0

# Customize the admin view for Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service', 'provider', 'date', 'time', 'status')
    list_filter = ('status', 'date', 'provider')
    search_fields = ('customer__username', 'provider__user__username', 'service__name')
    # inlines = [ReviewInline]  # Allowing reviews to be shown inline in the booking view

# Customize the admin view for Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'provider', 'rating')
    search_fields = ('customer__username', 'provider__user__username', 'comment')

# Customize the admin view for Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date', 'payment_method')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('booking__customer__username', 'booking__provider__user__username')

