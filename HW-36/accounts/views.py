from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm


# 1. Custom რეგისტრაციის View
class RegisterView(View):
    template_name = "accounts/register.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("profile")
        form = UserRegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("profile")
        return render(request, self.template_name, {"form": form})


# 2. Custom ლოგინის View
class LoginView(View):
    template_name = "accounts/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("profile")
        form = UserLoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)
            return redirect("profile")
        return render(request, self.template_name, {"form": form})


# 3. Custom ლოგაუთის View
class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect("home")

    def post(self, request):
        auth_logout(request)
        return redirect("home")


# 4. იუზერის პირადი გვერდი (Profile)
class ProfileView(LoginRequiredMixin, View):
    template_name = "accounts/profile.html"

    def get(self, request):
        return render(request, self.template_name, {"user": request.user})


# 5. იუზერის პროფილის განახლება (Update)
class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = "accounts/profile_edit.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
        return render(request, self.template_name, {"form": form})
