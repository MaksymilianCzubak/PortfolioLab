from django.shortcuts import render
from django.views import View
from .models import Donation, Institution
# Create your views here.

class LandingPage(View):
    def get(self, request):
        sum_of_sucks = Donation.objects.all().count()
        institutions = Institution.objects.all().count()
        ctx = {'sum_of_sucks': sum_of_sucks,
               'sum_of_institutions': institutions,
               }
        return render(request, "index.html", ctx)

class AddDonation(View):
    def get(self, request):
        ctx = {}
        return render(request, "form.html", ctx)

class Login(View):
    def get(self, request):
        ctx = {}
        return render(request, "login.html", ctx)

class Register(View):
    def get(self, request):
        ctx = {}
        return render(request, "register.html", ctx)