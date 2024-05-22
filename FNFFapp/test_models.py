from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        """ Create a user and a post to test """
        cls.user = User.objects.create_user(username='user', password='pass')
        cls.post = Post.objects.create(
            title='Test Title',
            author=cls.user,
            featured_image='placeholder',
            excerpt='Test excerpt',
            content='Test content',
            status=1,
        )

    def test_model_creation(self):
        """ Test post creation """
        self.assertIsInstance(self.post, Post)
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.featured_image, 'placeholder')
        self.assertEqual(self.post.excerpt, 'Test excerpt')
        self.assertEqual(self.post.content, 'Test content')

    def test_slug_generation(self):
        """ Test slug is automatically generated """
        post_without_slug = Post.objects.create(
            title='Post without slug',
            author=self.user,
            featured_image='placeholder',
            excerpt='Test excerpt',
            content='Test content',
            status=1,
        )
        self.assertIsNotNone(post_without_slug.slug)

    def test_number_of_likes(self):
        """ Test the number of likes method """
        usertwo = User.objects.create_user(username='usertwo', password='pass2')
        self.post.likes.add(usertwo)
        self.assertEqual(self.post.number_of_likes(),1)