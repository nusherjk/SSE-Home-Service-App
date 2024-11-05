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
    NECESSARY_FIELDS = ['first_name', 'last_name', 'username', 'email', 'dob', 'country', 'address', 'profession',
                        'C19Vaccinated', 'is_completed']

    def create_user(self, email, password=None, **extra_fields):

        if 'username' in extra_fields:
            username = extra_fields.pop('username')
        else:
            username = email.split('@')[0]

        # if password is None:
        #     return super().create_user(username=username, password=password, email=email,  **extra_fields)

        return super().create_user(username=username, password=password, email=email, **extra_fields)





    def get_n_fields(self):
        return self.NECESSARY_FIELDS



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
    address = models.ForeignKey("accounts.Address", on_delete=models.DO_NOTHING, null=True)

    country = CountryField(default="au")
    C19Vaccinated = models.BooleanField(default=False)
    profession = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    objects = CustomerManager()
    REQUIRED_FIELDS = []





class Address(models.Model):
    line1 = models.CharField(max_length=200, null=False)
    line2 = models.CharField(max_length=200, null=True)
    suburb = models.CharField(max_length=20, null=False)
    postcode = models.CharField(max_length=20, null=False)
    state = models.CharField(max_length=20, null=False)


    def __str__(self):
        return self.line1 + " " + self.line2 + ", "+ self.suburb + ", " + self.state + ", " + self.postcode + "."
    class Meta:
        verbose_name = 'Addresses'


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




