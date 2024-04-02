from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from OwDR_app.views import (
    IndexView,
    AddDonationView,
    LoginView,
    RegisterView,
    FormConfirmTemp,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),   # landing page
    path('accounts/login/', LoginView, name='login'),
    path('accounts/register/', RegisterView, name='register'),
    path('add-donation/', AddDonationView, name='add-donation'),
    path('conf-temp/', FormConfirmTemp, name='conf-temp'), # temp url
]
