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
    author_name = forms.CharField(max_length=200, initial="author")
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'author_name'
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "a" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     if not "e" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("com"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email

class RawArticleForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"}))
    author_name       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"author's name"}))
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
    

