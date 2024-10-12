from django.core.checks import messages
from django.shortcuts import render, redirect
# from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Customer
from .forms import CustomerRegisterForm
# AddressBook)
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse


# from rest_framework_simplejwt.serializers import TokenObtainSerializer
# Create your views here.
from .utils import send_welcome_email

class RegisterView(FormView):
    template_name = 'Auth/register.html'
    form_class = CustomerRegisterForm
    success_url = 'login'
    def form_valid(self, form):
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        form = CustomerRegisterForm(request.POST)
        email = form.data['email']
        password = form.data['password']

        if Customer.objects.filter(email=email).exists():
            # messages.add_message(self.request, messages.ERROR, "User already exists! Please Try and login!")
            return redirect('register')
        user = Customer.objects.create_user(email=email,
                                     password=password,
                                     )





        return redirect('login')


class NewLoginView(LoginView):
    template_name = 'Auth/login.html'


from django.shortcuts import redirect
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
# class AddressViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = AddressSerializer
#     queryset = AddressBook.objects.all()
#
#
#     def get_queryset(self):
#         instances = AddressBook.objects.filter(user=self.request.user)
#         return instances
#
#
#
# class CustomTokenObtainViewSet(TokenObtainPairView):
#     serializer_class =CustomTokeObtainSerializer