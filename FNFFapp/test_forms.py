from django.test import TestCase
from .models import Comment, Post
from .forms import CommentForm, PostForm
from django_summernote.widgets import SummernoteWidget


class CommentFormTest(TestCase):
    """ Test that form uses correct model and fields"""
    
    def test_form_model(self):
        self.assertEqual(CommentForm._meta.model, Comment)

    def test_form_fields(self):
        self.assertEqual(CommentForm._meta.fields, ('body',))


class PostFormTest(TestCase):
    """ Test that form uses correct model and fields """
    
    def test_form_model(self):
        self.assertEqual(PostForm._meta.model, Post)

    def test_form_fields(self):
        self.assertEqual(set(PostForm._meta.fields), set(('title', 'content', 'featured_image', 'excerpt')))

    def test_content_widget(self):
        self.assertIsInstance(PostForm._meta.widgets['content'], SummernoteWidget)

    def test_excerpt_widget(self):
        self.assertIsInstance(PostForm._meta.widgets['excerpt'], SummernoteWidget)

