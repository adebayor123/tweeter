from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': "Your message",
               'class': "form-control"}))
    class Meta:
        model = Tweet
        fields = [
            #"user",
            "content",
        ]
        # exclude = []

    # def clean_content(self, *args, **kwargs):
    #     # Validation overriding. cleaned_data will return original valid data input,
    #     # but we want to make new restrictions.
    #     # we name it clean_(field)
    #     content = self.cleaned_data.get("content")
    #     if content == "abc":
    #         raise forms.ValidationError("Cannot be ABC it's on model form")
    #     return content