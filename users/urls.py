from django.urls import path
from .views import UserSignup, UserLogin, UserLogout, PasswordResetRequest, PasswordResetConfirm, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('signup/', UserSignup.as_view(), name='user-signup'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    path('password-reset/', PasswordResetRequest.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password-reset-confirm'),
]