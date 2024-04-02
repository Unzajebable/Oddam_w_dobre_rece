from django.shortcuts import render
from django.views import View


class IndexView(View):
    """
    Straight-forward landing page rendering for the application
    """
    def get(self, request, *args, **kwargs):
        template_name = "OwDR_app/index.html"
        return render(request, template_name)


def AddDonationView(request, *args, **kwargs):
    return render(request, "OwDR_app/form.html")


def LoginView(request, *args, **kwargs):
    return render(request, "OwDR_app/login.html")


def RegisterView(request, *args, **kwargs):
    return render(request, "OwDR_app/register.html")


def FormConfirmTemp(request, *args, **kwargs):
    return render(request, "OwDR_app/form-confirmation.html")