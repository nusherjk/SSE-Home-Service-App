from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Address


# , AddressBook, OTP)



# Register your models here.
@admin.register(Customer)
class UserModel(UserAdmin):
    list_display = Customer.objects.get_n_fields()


@admin.register(Address)
class AddressModel(ModelAdmin):
    list_display = ['id','line1', 'line2', 'suburb', 'state', 'postcode']
#
#
# @admin.register(OTP)
# class OTPModel(ModelAdmin):
#     list_display = ['user','otp', 'created_at']