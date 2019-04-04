from django import forms

from .models import Product

'''
this is a pure Django way to show a form in the view.
This overrides all the previous ways to show the same data fields.
'''

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Your title', widget=forms.TextInput(attrs={"placeholder":"your title", "class":"input-group-sm"}))
    email       = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control-sm"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "class": "input-group-text",
                                    "id": "my-id-for-textarea",
                                    "rows": 5,
                                    "cols": 20
                                }
                            )
                        )
    price       = forms.DecimalField(initial=199.99, widget=forms.TextInput(attrs={"type":"number", "class":"input-group-sm"}))
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "a" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "e" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("com"):
            raise forms.ValidationError("This is not a valid email")
        return email

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price       = forms.DecimalField(initial=199.99)

