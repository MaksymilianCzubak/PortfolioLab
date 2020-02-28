from django.shortcuts import render, redirect
from django.views import View
from .models import Donation, Institution, User, Category
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

class LandingPage(View):
    def get(self, request):
        sum_of_sucks = Donation.objects.all().count()
        institutions = Institution.objects.all().count()
        wosp = Institution.objects.all().get(pk=1)
        wosp_name = wosp.name
        wosp_description = wosp.description
        ss = Institution.objects.all().get(pk=7)
        ss_name = ss.name
        ss_description = ss.description
        argos = Institution.objects.all().get(pk=8)
        argos_name = argos.name
        argos_description = argos.description
        ptsr = Institution.objects.all().get(pk=2)
        ptsr_name = ptsr.name
        ptsr_description = ptsr.description
        avalon = Institution.objects.all().get(pk=9)
        avalon_name = avalon.name
        avalon_description = avalon.description
        pzn_op = Institution.objects.all().get(pk=10)
        pzn_op_name = pzn_op.name
        pzn_op_description = pzn_op.description
        pfsp = Institution.objects.all().get(pk=11)
        pfsp_name = pfsp.name
        pfsp_description = pfsp.description
        zb_choinek = Institution.objects.all().get(pk=3)
        zb_choinek_name = zb_choinek.name
        zb_choinek_description = zb_choinek.description
        karetka = Institution.objects.all().get(pk=12)
        karetka_name = karetka.name
        karetka_description = karetka.description
        ctx = {'sum_of_sucks': sum_of_sucks,
               'sum_of_institutions': institutions,
               "wosp_name": wosp_name,
               "wosp_description": wosp_description,
               "ss_name": ss_name,
               "ss_description": ss_description,
               "argos_name": argos_name,
               "argos_description": argos_description,
               "ptsr_name": ptsr_name,
               "ptsr_description": ptsr_description,
               "avalon_name": avalon_name,
               "avalon_description": avalon_description,
               "pzn_op_name": pzn_op_name,
               "pzn_op_description": pzn_op_description,
               "pfsp_name": pfsp_name,
               "pfsp_description": pfsp_description,
               "zb_choinek_name": zb_choinek_name,
               "zb_choinek_description": zb_choinek_description,
               "karetka_name": karetka_name,
               "karetka_description": karetka_description,

               }
        return render(request, "index.html", ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'add_donation'

    def get(self, request):
        categories = Category.objects.all()
        ctx = {'categories': categories}
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, "form.html", ctx)


class AdminPanel(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = 'admin'
    redirect_field_name = 'admin'

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        ctx = {"form": form}
        return render(request, "register.html", ctx)

    def post(self, request):
        form = RegisterForm(request.POST)
        ctx = {"form": form}
        if form.is_valid():
            password2 = form.cleaned_data["password2"]
            first_name = form.cleaned_data["first_name"]
            username = form.cleaned_data["username"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if password == password2:
                User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,

                )
                messages.success(request, "Udało się stworzyć konto")
                return redirect("/login")
            else:
                form.add_error("password2", "Hasła nie są zgodne")
        return render(request, "register.html", ctx)


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)
        print(user.username)
        print(user.is_authenticated)
        if user is None:
            form.add_error(None, "Zły email lub hasło")
            return super().form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class UserView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, "user_data.html")



'''    login_url = 'login'
    redirect_field_name = 'add_donation'

    def get(self, request):
        categories = Category.objects.all()
        ctx = {'categories': categories}
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, "form.html", ctx)'''
