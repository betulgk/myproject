from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "post_name", "post_content")

    def clean_content(self):
        content = self.cleaned_data['post_content']

        return content

