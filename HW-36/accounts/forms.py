from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# 1. Custom იუზერის რეგისტრაციის ფორმა
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="პაროლი",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "შეიყვანეთ პაროლი"}),
    )
    password_confirm = forms.CharField(
        label="გაიმეორეთ პაროლი",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "გაიმეორეთ პაროლი"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "მომხმარებლის სახელი"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "ელ-ფოსტა"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "სახელი"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "გვარი"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("ეს ელ-ფოსტა უკვე გამოყენებულია.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "პაროლები ერთმანეთს არ ემთხვევა.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# 2. Custom ლოგინის ფორმა
class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="მომხმარებლის სახელი",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "მომხმარებლის სახელი"}),
    )
    password = forms.CharField(
        label="პაროლი",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "პაროლი"}),
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user = authenticate(username=username, password=password)
            if not self.user:
                raise forms.ValidationError("მომხმარებლის სახელი ან პაროლი არასწორია.")
            if not self.user.is_active:
                raise forms.ValidationError("ანგარიში დაბლოკილია.")
        return self.cleaned_data

    def get_user(self):
        return self.user


# 3. Custom იუზერის პროფილის განახლების ფორმა
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("ეს ელ-ფოსტა უკვე გამოყენებულია სხვა მომხმარებლის მიერ.")
        return email
