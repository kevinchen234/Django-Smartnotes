from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "home/register.html"
    success_url = "/smart/notes/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)
