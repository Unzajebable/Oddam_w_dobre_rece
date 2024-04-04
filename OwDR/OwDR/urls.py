from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from OwDR_app.views import (
    IndexView,
    AddDonationView,
    AddUserView,
    LoginView,
    LogoutView,
    FormConfirm,
)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', IndexView.as_view(), name='index'),   # landing page
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/register/', AddUserView.as_view(), name='register'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('add-donation/', login_required(AddDonationView), name='add-donation'),
    path('donation-confirmation/', login_required(FormConfirm), name='dono-conf'),
]
