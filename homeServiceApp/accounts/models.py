import datetime
from datetime import timezone, timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django_countries.fields import CountryField
from django.utils import timezone
# from django.dispatch import receiver
# from django.core.files.storage import default_storage
# from django.db.models.signals import pre_save, post_delete

# Create your models here.


class CustomerManager (UserManager):

    def create_user(self, email, password=None, **extra_fields):

        if 'username' in extra_fields:
            username = extra_fields.pop('username')
        else:
            username = email.split('@')[0]

        # if password is None:
        #     return super().create_user(username=username, password=password, email=email,  **extra_fields)

        return super().create_user(username=username, password=password, email=email, **extra_fields)


class Customer(AbstractUser):
    '''
     name, age, mobile,
email, country of citizenship, language preferred, Covid-19 vaccinated or not, or credit card bundle, trade,
and profession.
    '''
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField(default=timezone.now())

    country = CountryField(default="au")
    C19Vaccinated = models.BooleanField(default=False)
    profession = models.CharField(max_length=200)

    # email = models.EmailField(unique=True, primary_key=True)
    # # primary_address = models.CharField(max_length=2000, null=True, blank=True)
    # account_verified = models.BooleanField(default=False)
    # # profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
    #
    objects = CustomerManager()
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




# class OTP(models.Model):
#     user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING)
#     otp = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def is_valid(self):
#         return timezone.now() <= self.created_at + timedelta(minutes=5)

# @receiver(pre_save, sender=User)
# def delete_pre_existing_profile_picture(sender, instance, **kwargs):
#     if(instance.pk):
#         try:
#             obj = User.objects.get(pk=instance.pk)
#             if obj.profile_picture:
#                 if instance.profile_picture != obj.profile_picture:
#                     default_storage.delete(obj.profile_picture.path)
#         except User.DoesNotExist:
#             pass
#
#
# @receiver(post_delete, sender=User)
# def delete_post_profile_picture(sender, instance, **kwargs):
#     try:
#         default_storage.delete(instance.profile_picture.path)
#     except User.DoesNotExist:
#         pass



# class AddressBook(models.Model):
#     user = models.ForeignKey("accounts.User", on_delete=models.DO_NOTHING, related_name='user_address')
#     name = models.CharField(max_length=10, null=False, blank=False)
#     address = models.CharField(max_length=2000, null=False, blank=False)
#     Upozila = models.CharField(max_length=20, null=True, blank=True)
#     District = models.CharField(max_length=20, null=True, blank=True)
#     Division = models.CharField(max_length=20, null=True, blank=True)

