from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post, Comment, TeamMember


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
        usertwo = User.objects.create_user(username='usertwo', password='passtwo')
        self.post.likes.add(usertwo)
        self.assertEqual(self.post.number_of_likes(),1)


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Create a user, a post and a comment to test """
        cls.user = User.objects.create_user(username='user', password='pass')
        cls.post = Post.objects.create(title='Test Post', author=cls.user)
        now = timezone.now()     
        cls.comment1 = Comment.objects.create(
            post=cls.post,
            name='Jim Boy',
            email='jim@thesite.com',
            body='Second Comment.',
            created_on=now,
        )

        cls.comment = Comment.objects.create(
            post=cls.post,
            name='John Boy',
            email='jb@thesite.com',
            body='Test Comment.',
            created_on=now - timezone.timedelta(seconds=5)
        )
        
    def test_comment_creation(self):
        """ Test comment creation """
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.name, 'John Boy')
        self.assertEqual(self.comment.email, 'jb@thesite.com')
        self.assertEqual(self.comment.body, 'Test Comment.')
        self.assertIs(self.comment.approved, False)


    def test_comment_str(self):
        """ Test comment string """
        self.assertEqual(
            str(self.comment),
            'Comment Test Comment. by John Boy'
        )

    def test_comment_order(self):
        """ Test if comments are ordered by created_on (latest first) """
        comments = self.post.comments.all()
        self.assertEqual(comments[0], self.comment1)
        self.assertEqual(comments[1], self.comment)


class TeamMemberModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Creat team member to test"""
        cls.team_member = TeamMember.objects.create(
            name='Josey Girl', bio='Big horror fan! Death to romcoms!!')

    def test_team_member_creation(self):
        """ Test team member creation """
        self.assertIsInstance(self.team_member, TeamMember)
        self.assertEqual(self.team_member.name, 'Josey Girl')
        self.assertEqual(self.team_member.bio, 'Big horror fan! Death to romcoms!!')

    def test_comment_str(self):
        """ Test team_member string """
        self.assertEqual(str(self.team_member),'Josey Girl')