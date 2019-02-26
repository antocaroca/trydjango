from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"}))
    email       = forms.EmailField()
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

class RawArticleForm(forms.Form):
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

