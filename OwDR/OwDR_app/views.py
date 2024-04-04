from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login, logout
from django.views.generic import CreateView, FormView, RedirectView
from django.core.paginator import Paginator
from django.contrib.auth.models import User #email as username

from .models import ORG_CHOICE, Category, Institution, Donation
from .forms import AddUserForm, LoginForm, AddDonationForm

class IndexView(View):
    """
    Straight-forward landing page rendering for the application
    """
    def get(self, request, *args, **kwargs):
        template_name = "OwDR_app/index.html"
        orgs_num = Institution.objects.all().count()
        dono_num = Donation.objects.all().count()
        # orgp = Institution.objects.filter(org_type=2)
        # zblok = Institution.objects.filter(org_type=3)
        paginatorF = Paginator(Institution.objects.filter(org_type=1), 3)
        page_f_number = request.GET.get("pagef")
        page_f_obj = paginatorF.get_page(page_f_number)
        paginatorP = Paginator(Institution.objects.filter(org_type=2), 3)
        page_p_number = request.GET.get("pagep")
        page_p_obj = paginatorP.get_page(page_p_number)
        paginatorL = Paginator(Institution.objects.filter(org_type=3), 3)
        page_l_number = request.GET.get("pagel")
        page_l_obj = paginatorL.get_page(page_l_number)
        context = {
            "orgs": orgs_num,
            "donos": dono_num,
            "page_f_obj": page_f_obj,
            "page_p_obj": page_p_obj,
            "page_l_obj": page_l_obj,
        }
        return render(request, template_name, context)


def AddDonationView(request, *args, **kwargs):
    """
    Creation of a new donation
    """
    logged_user = request.user
    form = AddDonationForm()
    
    if request.method == 'POST':
        form = AddDonationForm(request.POST)
        if form.is_valid():
            new_dono = form.save(commit=False)
            new_dono.user = logged_user
            new_dono.save()
            return redirect('/donation-confirmation/')
    
    context = {
        "form": form,
    }
    return render(request, "OwDR_app/form.html", context)


class AddUserView(CreateView):
    """
    New user creation using CreateView and AddUserForm that inherits from UserCreationForm (all authentication
    of passwords, usernames, emails etc. handled by Django middlewares) - basically, Django does the heavy lifting here
    if you provide needed resources based on the documentation
    """
    template_name = "OwDR_app/register.html"
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy("login")


class LoginView(FormView):
    """
    Login view that logs you if provided with proper credentials
    """
    template_name = "OwDR_app/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("add-donation")

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return redirect('/accounts/register/')
        # response = super().form_invalid(form)
        # response
    


class LogoutView(RedirectView):
    """
    Logout view that logs out the user
    """
    url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


def FormConfirm(request, *args, **kwargs):
    return render(request, "OwDR_app/form-confirmation.html")