from django import forms
from .models import post


class postForm(forms.ModelForm):

    class Meta:

        model = post
        fields = ("post_name","post_content" )


