from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '.edu' not in email:
            raise forms.ValidationError("Please ude valid .edu email")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # validatinon code here
        return full_name


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1024)
