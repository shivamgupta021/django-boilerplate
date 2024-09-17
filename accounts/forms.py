from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            "image": forms.FileInput(),
            "display_name": forms.TextInput(attrs={"placeholder": "Add display name"}),
            "about": forms.Textarea(
                attrs={"rows": 5, "placeholder": "Add about yourself"}
            ),
        }


class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email"]
