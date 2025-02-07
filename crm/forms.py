from django import forms
from crm.models import Review,Product


class AddReview(forms.ModelForm):

    class Meta:

        model=Review

        fields="__all__"


class Addproduct(forms.ModelForm):

    class Meta:

        model=Product

        fields="__all__"