from django.shortcuts import render
from django.views import View
# Create your views here.

class LandingPage(View):
    def get(self, request):
        ctx = {}
        return render(request, "index.html", ctx)

class AddDonation(View):
    def get(self, request):
        ctx = {}
        return render(request, "index.html", ctx)

class Login(View):
    def get(self, request):
        ctx = {}
        return render(request, "login.html", ctx)

class Register(View):
    def get(self, request):
        ctx = {}
        return render(request, "register.html", ctx)