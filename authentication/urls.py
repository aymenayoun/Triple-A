from .views import RegistrationView,UsernameValidView,EmailValidView,VerificationView,LoginView,LogoutView,RequestPasswordResetEmail,CompletePasswordReset
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistrationView.as_view(),name='register'),
    path('validate-username',csrf_exempt(UsernameValidView.as_view()),name='validate_username'),
    path('validate-email',csrf_exempt(EmailValidView.as_view()),name='validate_email'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate'),
    path('login',LoginView.as_view(),name='login'),
    path('logout', LogoutView.as_view(), name='logout'), 
    path('request-reset-link', RequestPasswordResetEmail.as_view(), name='request-password'),
    path('set-new-password/<uidb64>/<token>/', CompletePasswordReset.as_view(), name='reset-user-password'), 
]
