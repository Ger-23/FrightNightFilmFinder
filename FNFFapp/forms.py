from .models import Comment, Post
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'featured_image', 'content', 'slug']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
