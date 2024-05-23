from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Comment, TeamMember
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

    def test_uses_indext_template(self):
        """ Tests that view uses correct template """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    
class PostDetailTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user', password='pass')
        self.client.login(username='user', password='pass')
        self.published_post = Post.objects.create(
            title='Test Post', slug='test-post', author=self.user, excerpt='Test except', content='Test content', status=1,)
        self.comment = Comment.objects.create(post=self.published_post, body='Test comment', approved=True)
        self.published_post.likes.add(self.user)

    def test_get_view_uses_correct_template(self):
        """ Test that Get view uses the specified template """
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.published_post.slug}))
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_view_saves_valid_comment(self):
        """ Test that Post view saves valid comment """
        data = {'content': 'Test comment'}
        response = self.client.post(reverse('post_detail', kwargs={'slug': self.published_post.slug}), data=data)

        self.assertContains(response, 'Test comment')
        self.assertEqual(Comment.objects.filter(post=self.published_post, body='Test comment').count(), 1)

class PostLikeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='pass')
        self.post = Post.objects.create(title='Test Post', content='Test content', author=self.user)

    def test_like_post(self):
        """ Test that liking a post adds user to likes list """
        self.client.login(username='user', password='pass')
        response = self.client.post(reverse('post_like', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertTrue(self.user in self.post.likes.all())


class TeamMemberDetailsTest(TestCase):

    def setUp(self):
        self.client = Client()
        TeamMember.objects.create(name='John Boy', bio='Admin')
        TeamMember.objects.create(name='Jam Bag', bio='Support')

    def test_view_context_contains_team_members(self):
        """ Test that view contains a list of team members and details """
        response = self.client.get(reverse('about'))
        self.assertIn('team_members', response.context)
        team_member = (response.context['team_members'][0])
        self.assertEqual(team_member.name, 'John Boy')
        self.assertEqual(team_member.bio, 'Admin')



    


