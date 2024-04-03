from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.models import User #email as username
from .models import ORG_CHOICE, Category, Institution, Donation

class IndexView(View):
    """
    Straight-forward landing page rendering for the application
    """
    def get(self, request, *args, **kwargs):
        template_name = "OwDR_app/index.html"
        orgs_num = Institution.objects.all().count()
        dono_num = Donation.objects.all().count()
        fundacje = Institution.objects.filter(org_type=1)
        orgp = Institution.objects.filter(org_type=2)
        zblok = Institution.objects.filter(org_type=3)
        # paginator = Paginator(fundacje, 3)    to do 
        context = {
            "orgs": orgs_num,
            "donos": dono_num,
            "fundacje": fundacje,
            "poza": orgp,
            "lokal": zblok,
        }
        return render(request, template_name, context)


def AddDonationView(request, *args, **kwargs):
    return render(request, "OwDR_app/form.html")


def LoginView(request, *args, **kwargs):
    return render(request, "OwDR_app/login.html")


def RegisterView(request, *args, **kwargs):
    return render(request, "OwDR_app/register.html")


def FormConfirmTemp(request, *args, **kwargs):
    return render(request, "OwDR_app/form-confirmation.html")