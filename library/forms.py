from django import forms

from .models import Book
from .models import Author


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'lastname', 'nickname']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if '.edu' not in email:
    #         raise forms.ValidationError("Please ude valid .edu email")
    #     return email

    # def clean_full_name(self):
    #     full_name = self.cleaned_data.get('full_name')
    #     # validation code here
    #     return full_name
