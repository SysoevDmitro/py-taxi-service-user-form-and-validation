from django.contrib.auth.forms import UserCreationForm
from .models import Driver, Car
from django import forms
from django.core.exceptions import ValidationError


class DriverLicenseCreateForm(UserCreationForm):

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",
                                                 "first_name",
                                                 "last_name")

    def clean_license_number(self):
        license = self.cleaned_data["license_number"]
        if len(license) != 8:
            raise ValidationError(
                "License number should consist of 8 characters")
        if not license[:3].isalpha() or not license[:3].isupper():
            raise ValidationError(
                "First 3 characters should be uppercase letters")
        if license[:3].isupper() and not license[-5:].isdigit():
            raise ValidationError("Last 5 characters should be digits")
        return license


class DriverLicenseUpdateForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        license = self.cleaned_data["license_number"]
        if len(license) != 8:
            raise ValidationError(
                "License number should consist of 8 characters")
        if not license[:3].isalpha() or not license[:3].isupper():
            raise ValidationError(
                "First 3 characters should be uppercase letters")
        if license[:3].isupper() and not license[-5:].isdigit():
            raise ValidationError("Last 5 characters should be digits")
        return license


class CarCreateForm(forms.ModelForm):
    drivers = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = Car
        fields = "__all__"
