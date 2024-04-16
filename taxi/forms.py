from django.contrib.auth.forms import UserCreationForm
from .models import Driver, Car
from django import forms


class DriverLicenseCreateForm(UserCreationForm):

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",
                                                 "first_name",
                                                 "last_name")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of 8 characters.")
        if not license_number[:3].isupper():
            raise forms.ValidationError(
                "First 3 characters must be uppercase letters.")
        if not license_number[3:].isdigit():
            raise forms.ValidationError(
                "Last 5 characters must be digits.")
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise forms.ValidationError(
                "License number must consist of 8 characters.")
        if not license_number[:3].isupper() or license_number[:3].isdigit():
            raise forms.ValidationError(
                "First 3 characters must be uppercase letters.")
        if not license_number[3:].isdigit():
            raise forms.ValidationError("Last 5 characters must be digits.")
        return license_number


class CarCreateForm(forms.ModelForm):
    drivers = forms.ModelChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = Car
        fields = "__all__"
