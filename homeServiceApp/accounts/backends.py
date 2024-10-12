# from django.contrib.auth.backends import ModelBackend
# # from django.contrib.auth.models import User
# from django.apps import apps
# from django.contrib import messages
# from .models import User
#
#
# class UserBackend(ModelBackend):
#     pass
    # # BranchUserModel = apps.get_model('usermodel.BranchUser', require_ready=False)
    # # SfUniteModel = apps.get_model('usermodel.SFUnit', require_ready=False)
    #
    # def authenticate(self, request, **kwargs):
    #     username = self.domainMailCheck(kwargs['username'])
    #     # username = kwargs['username']
    #     password = kwargs['password']
    #
    #
    #     try:
    #         user = User.objects.get(email=username)
    #         if ldapcheck(username, password) is True:
    #
    #             return user
    #         else:
    #             messages.add_message(request, messages.ERROR, 'Username or Password mismatch!')
    #     except User.DoesNotExist:
    #         messages.add_message(request, messages.ERROR, 'User does not Exist!')
    #
    #
    # # def get_user(self, user_id):
    # #     try:
    # #         # user = UserModel._default_manager.get(pk=user_id)
    # #         # if(self.SfUniteModel._default_manager.get(pk=user_id)):
    # #         #     use
    # #     except UserModel.DoesNotExist:
    # #         return None
    # #     return user if self.user_can_authenticate(user) else None