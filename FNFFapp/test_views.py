from django.test import TestCase, Client
from .models import Post
from django.contrib.auth.models import User

class PostListTest(TestCase):

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.user = kwargs.get('user')

    def setUp(self):
        if not self.user:
            self.user = User.objects.create_user(username='user', password='pass')
        self.published_post1 = Post.objects.create(title="Published Post 1", status=1, created_on='23-05-24', author=self.user)
        self.published_post2 = Post.objects.create(title="Published Post 2", status=1, created_on='22-05-24', author=self.user)
        self.draft_post = Post.objects.create(title="Draft Post", status=0, created_on='21-05-24', author=self.user)
        self.client = Client()

    def test_get_published_post(self):
        """ Test that view returns published posts, ordered by creation date """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        context = response.context
        posts = context['object_list']
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].title, self.published_post2.title)
        self.assertEqual(posts[1].title, self.published_post1.title)

