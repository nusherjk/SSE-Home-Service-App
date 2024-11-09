from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.urls import reverse_lazy

from .models import Customer
from .forms import CustomerRegisterForm, AddressForm, UpdateProfileForm
from django.views.generic import TemplateView, FormView, UpdateView, RedirectView
from django.contrib.auth.views import LoginView


class RegisterView(FormView):
    template_name = 'Auth/bregister.html'
    form_class = CustomerRegisterForm
    success_url = 'login'
    def form_valid(self, form):
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            C19Vaccinated = form.cleaned_data['C19Vaccinated']
            profession = form.cleaned_data['profession']

            if Customer.objects.filter(email=email).exists():

                user = Customer.objects.get(email=email)
                if user.is_completed:
                # messages.add_message(self.request, messages.ERROR, "User already exists! Please Try and login!")
                    return redirect('register')
                else:
                    pass_verified = user.check_password(password)

                    user.C19Vaccinated = C19Vaccinated
                    user.profession = profession
                    user.country = country
                    user.is_completed = True
                    user.save()
                    print("user Updated")

            else:
                user = Customer.objects.create_user(email=email,
                                         password=password,
                                                first_name=first_name,
                                                last_name=last_name,
                                                country=country,
                                                C19Vaccinated=C19Vaccinated,
                                                profession=profession,
                                                is_completed=True
                                         )





            return redirect('login')


class NewLoginView(LoginView):
    template_name = 'Auth/blogin.html'


from django.shortcuts import redirect


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Auth/buserProfiles.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_provider'] = False
        context['addressform'] = AddressForm()
        context['upadteprofile'] = UpdateProfileForm(instance=self.request.user)
        if apps.get_model('core', 'ProviderProfile').objects.filter(user=self.request.user).exists():
            context['is_provider'] = True
            context['user_additional'] = apps.get_model('core', 'ProviderProfile').objects.get(user=self.request.user)


        return context


    def post(self,*args, **kwargs):
        form = AddressForm(self.request.POST)
        if form.is_valid():
            address = form.save()
            self.request.user.address = address
            self.request.user.save()
        self.request.user.is_completed = True
        #     Check Profile is complete or not
        for items in Customer.objects.get_n_fields():
            print(getattr(self.request.user, items))
            if getattr(self.request.user, items) is None:
                print(items + " Is empty")
                self.request.user.is_completed = False
        self.request.user.save()


        return redirect('profile')



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = UpdateProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Return the currently logged-in user as the object to be updated
        return self.request.user





# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from allauth.socialaccount.helpers import complete_social_login
from django.conf import settings


# def google_login(request):
#     """
#     Redirects the user directly to the Google OAuth login.
#     """
#     client_id = settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id']
#     callback_url = request.build_absolute_uri('/accounts/oauth/google/login/callback/')
#
#     oauth_client = OAuth2Client(callback_url=callback_url)
#     google_adapter = GoogleOAuth2Adapter(request)
#     return google_adapter.login(request, oauth_client)

# from .models import OTP
# from .utils import generate_otp, send_otp_email  # Import the helper functions
#
# def send_otp(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         otp = generate_otp()
#         send_otp_email(email, otp)
#
#         # Store OTP in the database
#         OTP.objects.create(email=email, otp=otp)
#
#         return render(request, 'otp_sent.html', {'message': 'OTP sent to your email!'})
#     return render(request, 'send_otp.html')
#
#
# def verify_otp(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         otp_entered = request.POST.get('otp')
#
#         # Get the OTP record for this email
#         try:
#             otp_record = OTP.objects.get(email=email, otp=otp_entered)
#             if otp_record.is_valid():
#                 return HttpResponse('OTP successfully verified!')
#             else:
#                 return HttpResponse('OTP has expired.')
#         except OTP.DoesNotExist:
#             return HttpResponse('Invalid OTP.')
#
#     return render(request, 'verify_otp.html')


# class UserViewSet(ReadOnlyModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#
#
# class UserView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#     def get_object(self):
#         instance = self.request.user
#         return instance
#
# class AddressView(LoginRequiredMixin, TemplateView):
#     def get_queryset(self):
#         instances = Address.objects.filter(user=self.request.user)
#         return instances
#
#
#
# class CustomTokenObtainViewSet(TokenObtainPairView):
#     serializer_class =CustomTokeObtainSerializer
