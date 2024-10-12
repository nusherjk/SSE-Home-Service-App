from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
# , AddressBook, OTP)



# Register your models here.
@admin.register(Customer)
class UserModel(UserAdmin):
    list_display = ['username', 'email']


# @admin.register(AddressBook)
# class AddressModel(ModelAdmin):
#     list_display = ['id','name', 'address']
#
#
# @admin.register(OTP)
# class OTPModel(ModelAdmin):
#     list_display = ['user','otp', 'created_at']