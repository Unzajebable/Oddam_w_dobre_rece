from django.contrib import admin
from .models import ORG_CHOICE, Category, Institution, Donation


admin.site.register(Category)


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "org_type")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("user", "institution", "phone_number")
