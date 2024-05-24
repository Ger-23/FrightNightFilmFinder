from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    """
    Form for creating and editing Post instances.
    Uses SummernoteWidget text editing of 'content' and
    'excerpt' fields.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt']
        widgets = {
            'content': SummernoteWidget(),
            'excerpt': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    """
    Form for creating Comment Instances.
    """
    class Meta:
        model = Comment
        fields = ('body',)

